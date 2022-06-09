from api.game_classes.creatures.hero import Hero
from api.web.WebService import *


class User:
    def __init__(self):
        self.nick = None
        self.email = None
        self.sex = None
        self.age = None
        self.UID = None

        self.heroes_min_info = {}
        self.heroes = {}

        self.currentHero = None
        self.authUser = None

        self.enemy_heroes_min_info = {}
        self.enemy_heroes = {}

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

                self.get_heroes_min_info()

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

    def get_heroes_min_info(self):
        conn, cursor = connect_to_db()
        with conn:
            try:
                cursor.execute("SELECT hero_id,name,avatar_id,level_id,hero_class FROM heroes WHERE PLAYER_ID = %s",
                               (self.UID,))
                from_heroes = cursor.fetchall()
                for i in from_heroes:
                    self.heroes_min_info[i[0]] = i
            except Exception as error:
                print(error)

    def get_enemy_heroes_min_info(self):
        conn, cursor = connect_to_db()
        with conn:
            try:
                cursor.execute("SELECT hero_id,name,avatar_id,level_id,hero_class FROM heroes WHERE PLAYER_ID != %s",
                               (self.UID,))
                from_heroes = cursor.fetchall()
                for i in from_heroes:
                    self.enemy_heroes_min_info[i[0]] = i
            except Exception as error:
                print(error)

    def sign_up(self, email, password, nick, sex, age):
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

    def get_hero(self, hero_id, name, avatar_id, lvl, hero_class):
        conn, cursor = connect_to_db()
        with conn:
            try:
                cursor.execute(
                    "SELECT exp,exp_next_lvl,free_development_pts,statistics_id FROM heroes WHERE HERO_ID = %s",
                    (hero_id,))
                h = cursor.fetchone()
                cursor.execute("SELECT * FROM STATISTICS WHERE STATISTICS_ID = %s", (h[3],))
                s = cursor.fetchone()
                self.heroes[hero_id] = Hero(avatar_id, name, hero_class, s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8],
                                            s[9],
                                            s[10], lvl, h[0], h[1], h[2], hero_id, h[3])

            except Exception as error:
                print(error)

    def get_enemy_hero(self, hero_id, name, avatar_id, lvl, hero_class):
        conn, cursor = connect_to_db()
        with conn:
            try:
                cursor.execute(
                    "SELECT exp,exp_next_lvl,free_development_pts,statistics_id FROM heroes WHERE HERO_ID = %s",
                    (hero_id,))
                h = cursor.fetchone()
                cursor.execute("SELECT * FROM STATISTICS WHERE STATISTICS_ID = %s", (h[3],))
                s = cursor.fetchone()
                self.enemy_heroes[hero_id] = Hero(avatar_id, name, hero_class, s[1], s[2], s[3], s[4], s[5], s[6], s[7],
                                                  s[8],
                                                  s[9],
                                                  s[10], lvl, h[0], h[1], h[2], hero_id, h[3])

            except Exception as error:
                print(error)

    def choose_hero(self, hero_id):
        self.get_hero(*self.heroes_min_info[hero_id])
        self.currentHero = self.heroes[hero_id]

    def choose_enemy_hero(self, hero_id):
        self.get_enemy_hero(*self.enemy_heroes_min_info[hero_id])
        self.enemy_heroes[hero_id].gen_eq()

    def deselect_hero(self):
        self.currentHero = None

    def remove_hero(self, hero_id):
        conn, cursor = connect_to_db()
        with conn:
            try:
                cursor.execute("CALL remove_hero(%s)", (hero_id,))
            except Exception as error:
                print(error)

        if self.currentHero == self.heroes[hero_id]:
            self.currentHero = None
        self.heroes.pop(hero_id)

    def remove_me(self):
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

    def create_hero(self, avatar_id, name, className, strength, intelligence, dexterity, constitution,
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
                self.heroes[int(cursor.fetchone())] = newHero

            except Exception as error:
                print(error)


if __name__ == "__main__":
    tmp = User()
    # tmp.sign_up('enemy@gmail.com', 'alamakota', 'JohnDoe', 'f', 20)
    tmp.login('konto@gmail.com', 'alamakota')
    # tmp.login('enemy@gmail.com', 'alamakota')
    # tmp.create_hero(2, 'Dude', 'm', 1, 1, 1, 1,
    #                 1, 1, 1, 1, 1, 1)

    tmp.get_enemy_heroes_min_info()
    for _, val in tmp.enemy_heroes_min_info.items():
        print(_)
    # tmp.choose_hero(1)
    # print(tmp.currentHero)
    tmp.choose_enemy_hero(1)

    print(tmp.enemy_heroes[1])

    # tmp.choose_hero(20)
    # hero: Hero = tmp.currentHero
    # print(hero)

    # print(hero)
    # print("-------------------------")
    # print(hero.fight_with_bot_from_quest(0))
    # print("-------------------------fight")
    # print(hero)
