import time
import random

# ================= UI =================
print("═"*50)
print("      🎮 Welcome to CounterPick 🎮")
print("═"*50)

# ================= RULES =================
rules = """⇛ 🎮 LEAD vs COUNTER - GAME RULES

↪ 👥 ROLES:
    Lead = Goes first and earns points by surviving rounds
    Counter = Tries to predict Lead’s number and eliminate them

↪ ⚙️ SETUP:
    Choose a mode:
        1. CounterPick Vanilla
        2. CounterPick One-Up
    Flip a coin to decide Lead
    Both start with 0 points

↪ 🔁 HOW THE GAME WORKS:
    Each round:
    Both choose a number from 1 to 10
    Reveal at the same time

↪ 💥 RESULTS:

    ↪ IF numbers match:

        (Vanilla)
        Lead loses instantly ❌

        (One-Up)
        Lead survives and gets number² points 🔥

    ↪ IF numbers do NOT match:

        (Vanilla)
        Lead gets points equal to their number

        (One-Up)
        If Counter picks ±1 → Lead loses ❌
        Else → Lead gets points

↪ 🔄 ROLE SWAP:
    When Lead loses → roles switch

↪ 🏁 WIN CONDITION:
    Both players must be Lead once and lose once
    Highest score wins 🏆

↪ 💯 SCORING:
    Lead gains points equal to chosen number
    (One-Up match = square points)

    Counter gets 0 points

↪ 🧠 STRATEGY:
    Lead → Avoid prediction
    Counter → Predict or trap

END OF RULES
"""

# ================= GAME =================
class Game:
    def __init__(self, lead=None, counter=None):
        self.lead = lead
        self.counter = counter
        self.score = {"player": 0, "opponent": 0}

    @staticmethod
    def choose_heads_tails():
        print("\n🪙 Choose Heads or Tails!")

        while True:
            choice = input("▶ (h/t): ").lower().strip()

            if choice in ["h", "heads"]:
                user = "heads"
                opp = "tails"
                break
            elif choice in ["t", "tails"]:
                user = "tails"
                opp = "heads"
                break
            else:
                print("❌ Invalid choice, retry.")

        result = random.choice(["heads", "tails"])

        for i in range(6):
            print(f"🪙 Tossing coin{'.'*(i%4)}", end="\r")
            time.sleep(random.uniform(0.3, 0.7))

        print(" " * 30, end="\r")
        print(f"🪙 Result: {result}")

        if result == user:
            print("✅ You won the toss!")
            return "player"
        else:
            print("❌ Opponent won the toss!")
            return "opponent"

    def choose_lead_counter(self):
        chooser = self.choose_heads_tails()

        if chooser == "player":
            while True:
                print("\nChoose role (lead/counter)")
                choice = input("▶ ").lower().strip()

                if choice.startswith("l"):
                    self.lead = "player"
                    self.counter = "opponent"
                    break
                elif choice.startswith("c"):
                    self.lead = "opponent"
                    self.counter = "player"
                    break
                else:
                    print("❌ Invalid option.")
        else:
            if random.choice([True, False]):
                self.lead = "opponent"
                self.counter = "player"
                print("🤖 Opponent chose Lead 👑")
            else:
                self.lead = "player"
                self.counter = "opponent"
                print("🤖 Opponent chose Counter 🧠")

    @staticmethod
    def game_mode_choose():
        while True:
            print("\n🎮 Choose Game Mode:")
            print("1 - Vanilla")
            print("2 - One-Up")

            choice = input("▶ ").lower().strip()

            if choice in ["1", "vanilla"]:
                return VanillaGame()
            elif choice in ["2", "oneup", "one-up"]:
                return OneUpGame()
            else:
                print("❌ Invalid option.")

    def game_end(self):
        print("\n🏁 FINAL RESULT")
        if self.score["player"] > self.score["opponent"]:
            print(f"🎉 You won! ({self.score['player']})")
        elif self.score["opponent"] > self.score["player"]:
            print(f"💀 Opponent won! ({self.score['opponent']})")
        else:
            print("🤝 It's a tie!")

    def __str__(self):
        return (f"\n👑 Lead: {self.lead} | 🧠 Counter: {self.counter}\n"
                f"💯 You: {self.score['player']} | Opponent: {self.score['opponent']}")

# ================= VANILLA =================
class VanillaGame(Game):
    def __init__(self):
        super().__init__()

    def game_play(self):
        round_count = 0
        vanilla_first_lead = self.lead
        while True:
            if round_count == 1:
                if self.score[vanilla_first_lead] < self.score[self.lead]:
                    break

            print(self)

            choice = input("\n🎯 Choose number (1-10): ")

            if not choice.isdigit() or not (1 <= int(choice) <= 10):
                print("❌ Invalid input.")
                continue

            player_num = int(choice)

            for i in range(3):
                print(f"🤖 Opponent thinking{'.'*(i%4)}", end="\r")
                time.sleep(random.uniform(0.3, 0.7))
            print(" " * 30, end="\r")

            bot_num = random.randint(1, 10)

            print(f"\nYou: {player_num}")
            print(f"Opponent: {bot_num}")

            if player_num == bot_num:
                if self.lead == "player":
                    print(f"You lost the round with a score of {self.score['player']}")
                else:
                    print(f"Opponent lost the round with a score of {self.score['opponent']}")

                print("💥 MATCH! Lead loses!")

                round_count += 1
                self.lead, self.counter = self.counter, self.lead

                if round_count >= 2:
                    break
            else:
                if self.lead == "player":
                    self.score["player"] += player_num
                    print(f"➕ You gained {player_num}")
                else:
                    self.score["opponent"] += bot_num
                    print(f"➕ Opponent gained {bot_num}")

# ================= ONE-UP =================
class OneUpGame(Game):
    def __init__(self):
        super().__init__()

    def game_play(self):
        round_count = 0
        oneup_first_lead = self.lead
        while True:
            if round_count == 1:
                if self.score[oneup_first_lead] < self.score[self.lead]:
                    break

            print(self)

            choice = input("\n🎯 Choose number (1-10): ")

            if not choice.isdigit() or not (1 <= int(choice) <= 10):
                print("❌ Invalid input.")
                continue

            player_num = int(choice)

            for i in range(3):
                print(f"🤖 Opponent thinking{'.'*(i%4)}", end="\r")
                time.sleep(random.uniform(0.3, 0.7))
            print(" " * 30, end="\r")

            bot_num = random.randint(1, 10)

            print(f"\nYou: {player_num}")
            print(f"Opponent: {bot_num}")

            if abs(player_num - bot_num) == 1:
                if self.lead == "player":
                    print(f"You lost the round with a score of {self.score['player']}")
                else:
                    print(f"Opponent lost the round with a score of {self.score['opponent']}")

                print("💥 MATCH! Lead loses!")

                round_count += 1
                self.lead, self.counter = self.counter, self.lead

                if round_count >= 2:
                    break
            elif player_num != bot_num:
                if self.lead == "player":
                    self.score["player"] += player_num
                    print(f"➕ You gained {player_num} points")
                else:
                    self.score["opponent"] += bot_num
                    print(f"➕ Opponent gained {bot_num} points")
            else:
                print("💥 MULT! Squared points!")
                if self.lead == "player":
                    self.score["player"] += player_num**2
                    print(f"➕ You gained {player_num**2} points")
                else:
                    self.score["opponent"] += bot_num**2
                    print(f"➕ Opponent gained {bot_num**2} points")

# ================= MAIN LOOP =================
while True:
    print("\n📌 What would you like to do?")
    print("1 - View Rules 📜")
    print("2 - Play 🎮")
    print("3 - Exit 🚪")

    choice = input("▶ ").lower().strip()

    if choice in ["1", "rules"]:
        for i in range(6):
            print(f"📜 Loading rules{'.'*(i%4)}", end="\r")
            time.sleep(random.uniform(0.3, 0.7))
        print(" " * 30, end="\r")

        print(rules)
        input("\nPress Enter to continue...")

    elif choice in ["2", "play"]:
        game = Game.game_mode_choose()
        game.choose_lead_counter()
        game.game_play()
        game.game_end()

    elif choice in ["3", "exit"]:
        print("👋 Exiting game...")
        break

    else:
        print("❌ Invalid choice.")