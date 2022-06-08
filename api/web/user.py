from api.game_classes.creatures.hero import Hero
from api.web.WebService import *


class User:
    def __init__(self):
        self.nick = None
        self.email = None
        self.sex = None
        self.age = None
        self.UID = None
        self.Heroes = {}
        self.currentHero = None
        self.authUser = None

        self.all_heroes = None
        # self.all_heroes = self.getAllExistingHeroes()

    def login(self, email, password):
        login_status = None
        player_id = None
        conn, cursor = connect_to_db()
        with conn:
            try:
                self.authUser = auth.sign_in_with_email_and_password(email, password)
                player_id = self.authUser['localId']
                cursor.execute(
                    "select block_id from blocked_users where player_id = %s and current_timestamp < block_end order by block_end desc limit 1;",
                    (player_id,))
                if cursor.fetchone() is not None:
                    print("You are blocked")
                    login_status = False
                    return False
                cursor.execute("SELECT * FROM players WHERE player_id = %s;", (player_id,))
                user = cursor.fetchone()
                self.nick = user[0]
                self.email = user[1]
                self.sex = user[2]
                self.age = user[3]
                self.UID = user[4]
                self.getHeroes()

                """
                Jeśli będzie czas to można zamienić listę bohaterów na listę nazw bohaterów i dopiero po kliknięciu na bohatera ładowac jego szczegóły
                """

                print("Successfully logged in!")
                login_status = True
            except Exception as error:
                conn, cursor = connect_to_db()
                with conn:
                    try:
                        cursor.execute("select player_id from players where email = %s", (email,))
                        player_id = cursor.fetchone()
                    except Exception as db_error:
                        print(db_error, "\n***************\n")
                    finally:
                        print("Invalid email or password\n***************\n", error)
                        login_status = False
            finally:
                conn, cursor = connect_to_db()
                with conn:
                    try:
                        cursor.execute("CALL add_log(%s,%s)", (player_id, login_status))
                    except Exception as error:
                        print(error)
                    finally:
                        return login_status

    def signup(self, email, password, nick, sex, age):
        conn, cursor = connect_to_db()
        with conn:
            try:
                auth.create_user_with_email_and_password(email, password)
                self.authUser = auth.sign_in_with_email_and_password(email, password)
                cursor.execute("CALL add_player(%s ,%s , %s, %s, %s)",
                               (nick, email, sex, age, self.authUser['localId']))
                return True
            except Exception as error:
                print("Email already exists\n***************\n", error)
                return False

    @staticmethod
    def logout():
        auth.current_user = None

    def getHeroes(self):
        conn, cursor = connect_to_db()
        with conn:
            try:
                cursor.execute("SELECT * FROM HEROES WHERE PLAYER_ID = %s", (self.UID,))
                from_heroes = cursor.fetchall()
                for i in from_heroes:
                    cursor.execute("SELECT * FROM STATISTICS WHERE STATISTICS_ID = %s", (i[7],))
                    s = cursor.fetchone()
                    self.Heroes[i[2]] = Hero(i[11], i[0], i[6], i[3], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8],
                                             s[9],
                                             s[10], i[4], i[5], i[10], i[9], i[2], i[7])
            except Exception as error:
                print(error)

    def chooseHero(self, hero_id):
        self.currentHero = self.Heroes[hero_id]

    def deselectHero(self):
        self.currentHero = None

    def removeHero(self, hero_id):
        conn, cursor = connect_to_db()
        with conn:
            try:
                cursor.execute("CALL remove_hero(%s)", (hero_id,))
            except Exception as error:
                print(error)

        if self.currentHero == self.Heroes[hero_id]:
            self.currentHero = None
        self.Heroes.pop(hero_id)

    def removeMe(self):
        if self.authUser is not None:
            conn, cursor = connect_to_db()
            with conn:
                try:
                    cursor.execute("CALL remove_player(%s)", (self.UID,))
                    auth.delete_user_account(self.authUser['idToken'])
                    del User
                except Exception as error:
                    print(error)
        else:
            print("User not logged in - nothing to remove")

    def createHero(self, avatar_id, name, className, strength, intelligence, dexterity, constitution,
                   luck, persuasion, trade, leadership, protection, initiative):
        # className in ('a','w','m')
        conn, cursor = connect_to_db()
        with conn:
            try:
                cursor.execute("SELECT add_hero(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                               (avatar_id, name, self.UID, className, strength, intelligence, dexterity, constitution,
                                luck, persuasion, trade, leadership, protection, initiative))
                newHero = Hero(avatar_id, name, className, 0, strength, intelligence, dexterity, constitution,
                               luck, persuasion, trade, leadership, protection, initiative)
                self.Heroes[int(cursor.fetchone())] = newHero

            except Exception as error:
                print(error)

    @staticmethod
    def getAllExistingHeroes():
        all_existing_heroes = {}
        conn, cursor = connect_to_db()
        with conn:
            try:
                cursor.execute("SELECT * FROM HEROES")
                from_heroes = cursor.fetchall()
                for i in from_heroes:
                    cursor.execute("SELECT * FROM STATISTICS WHERE STATISTICS_ID = %s", (i[7],))
                    s = cursor.fetchone()
                    all_existing_heroes[i[2]] = Hero(i[11], i[0], i[6], i[3], s[1], s[2], s[3], s[4], s[5], s[6], s[7],
                                                     s[8], s[9],
                                                     s[10], i[4], i[5], i[10], i[9], i[2], i[7])
                return all_existing_heroes
            except Exception as error:
                print(error)
                return -1


if __name__ == "__main__":
    tmp = User()
    #     # tmp.signup('test@gmail.com', 'alamakota', 'Viciooo', 'm', 21)
    tmp.login('konto@gmail.com', 'alamakota')
    tmp.chooseHero(20)
    hero: Hero = tmp.currentHero
    print(hero.get_gold())
    # print(hero)
    # print("-------------------------")
    # print(hero.fight_with_bot_from_quest(0))
    # print("-------------------------fight")
    # print(hero)
