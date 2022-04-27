from backend.src.game_classes.creatures.hero import Hero
from backend.src.web.WebService import *


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
        self.all_heroes = self.getAllExistingHeroes()

    def login(self, email, password):
        try:
            self.authUser = auth.sign_in_with_email_and_password(email, password)
            conn, cursor = connect_to_db()
            cursor.execute("SELECT * FROM players WHERE player_id = %s;", (self.authUser['localId'],))
            user = cursor.fetchall()[0]
            self.nick = user[0]
            self.email = user[1]
            self.sex = user[2]
            self.age = user[3]
            self.UID = user[4]
            disconnect_from_db(conn, cursor)
            self.getHeroes()
            print("Successfully logged in!")
            return True
        except:
            print("Invalid email or password")
            return False

    def signup(self, email, password, nick, sex, age):
        try:
            auth.create_user_with_email_and_password(email, password)
            self.authUser = auth.sign_in_with_email_and_password(email, password)
            # TODO maybe unnecessary logout
            self.logout()
            conn, cursor = connect_to_db()

            cursor.execute("CALL add_player(%s ,%s , %s, %s, %s)", (nick, email, sex, age, self.authUser['localId']))
            conn.commit()

            disconnect_from_db(conn, cursor)
            return True
        except:
            print("Email already exists")
            return False

    # TODO may need further implementation
    def logout(self):
        auth.current_user = None

    def getHeroes(self):
        try:
            conn, cursor = connect_to_db()
            cursor.execute("SELECT * FROM HEROES WHERE PLAYER_ID = %s", (self.UID,))
            from_heroes = cursor.fetchall()
            print(from_heroes)
            for i in from_heroes:
                cursor.execute("SELECT * FROM STATISTICS WHERE STATISTICS_ID = %s", (i[7],))
                s = cursor.fetchall()[0]
                self.Heroes[i[2]] = Hero(i[0], i[6], i[3], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8], s[9],
                                         s[10], i[4], i[5], i[10], i[9], i[2], i[7])
            disconnect_from_db(conn, cursor)
        except Exception as error:
            print(error)

    def chooseHero(self, hero_id):
        self.currentHero = self.Heroes[hero_id]

    def removeHero(self, hero_id):
        try:
            conn, cursor = connect_to_db()
            cursor.execute("CALL remove_hero(%s)", (hero_id,))
            conn.commit()
            disconnect_from_db(conn, cursor)
        except Exception as error:
            print(error)

        if self.currentHero == self.Heroes[hero_id]:
            self.currentHero = None
        self.Heroes.pop(hero_id)

    def removeMe(self):
        if self.authUser is not None:
            try:
                conn, cursor = connect_to_db()
                cursor.execute("CALL remove_player(%s)", (self.UID,))
                conn.commit()
                disconnect_from_db(conn, cursor)
                auth.delete_user_account(self.authUser['idToken'])
                del User
            except Exception as error:
                print(error)
        else:
            print("User not logged in - nothing to remove")

    def createHero(self, name, className, strength, intelligence, dexterity, constitution,
                   luck, persuasion, trade, leadership, protection, initiative):
        # className in ('a','w','m')

        newHero = Hero(name, className, 0, strength, intelligence, dexterity, constitution,
                       luck, persuasion, trade, leadership, protection, initiative)
        try:
            conn, cursor = connect_to_db()
            cursor.execute("SELECT add_hero(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                           (name, self.UID, className, strength, intelligence, dexterity, constitution,
                            luck, persuasion, trade, leadership, protection, initiative))
            conn.commit()
            self.Heroes[int(cursor.fetchall()[0])] = newHero
            disconnect_from_db(conn, cursor)
        except Exception as error:
            print(error)

    @classmethod
    def getAllExistingHeroes(cls):
        try:
            all_existing_heroes = {}
            conn, cursor = connect_to_db()
            cursor.execute("SELECT * FROM HEROES")
            from_heroes = cursor.fetchall()
            for i in from_heroes:
                cursor.execute("SELECT * FROM STATISTICS WHERE STATISTICS_ID = %s", (i[7],))
                s = cursor.fetchall()[0]
                all_existing_heroes[i[2]] = Hero(i[0], i[6], i[3], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8], s[9],
                                                 s[10], i[4], i[5], i[10], i[9], i[2], i[7])
            disconnect_from_db(conn, cursor)
            return all_existing_heroes
        except Exception as error:
            print(error)
            return -1


if __name__ == "__main__":
    tmp = User()
    # tmp.signup('test@gmail.com', 'alamakota', 'Viciooo', 'm', 21)
    tmp.login('konto@gmail.com', 'alamakota')
    # tmp.createHero('testx', 'w', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    tmp.chooseHero(20)
    # tmp.currentHero.add_to_statistics('dexterity')
    # tmp.currentHero.add_to_statistics('luck')
    print(tmp.currentHero)
    tmp.currentHero.init_fight_with_other_hero(tmp.Heroes.get(19))
    # tmp.currentHero.armourShop.print()
    # tmp.currentHero.buy_from_shop(0, 0)
    # tmp.currentHero.buy_from_shop(0, 1)
    # tmp.currentHero.buy_from_shop(0, 2)
    # tmp.currentHero.buy_from_shop(0, 3)
    # tmp.currentHero.buy_from_shop(0, 4)
    # for i in User.getAllExistingHeroes().values():
    #     print(i)
