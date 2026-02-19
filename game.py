import random
import textwrap


class Player:
    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.focus = 100
        self.knowledge = 0
        self.xp = 0
        self.level = 1

    def is_alive(self) -> bool:
        return self.health > 0 and self.focus > 0

    def add_xp(self, amount: int) -> None:
        self.xp += amount
        while self.xp >= self.level * 40:
            self.xp -= self.level * 40
            self.level += 1
            self.health = min(100, self.health + 15)
            self.focus = min(100, self.focus + 10)
            self.knowledge += 10
            print(f"\n⚡ LEVEL UP! You are now Level {self.level}.")
            print("+15 Health, +10 Focus, +10 Knowledge")


BASIC_QUESTIONS = [
    ("What is 12 + 18?", "30"),
    ("What planet is known as the Red Planet?", "mars"),
    ("Binary of decimal 5?", "101"),
    ("Who wrote the Indian National Anthem?", "tagore"),
    ("What is 9 x 7?", "63"),
    ("H2O is the chemical formula of?", "water"),
    ("What is 15% of 200?", "30"),
    ("CPU stands for?", "central processing unit"),
    ("Square root of 144?", "12"),
    ("Fastest land animal?", "cheetah"),
]

RAPID_FIRE = [
    ("2^5 = ?", "32"),
    ("Capital of Japan?", "tokyo"),
    ("11 x 11 = ?", "121"),
    ("Primary language for Android apps by Google today?", "kotlin"),
    ("What gas do plants absorb?", "carbon dioxide"),
    ("First element in periodic table?", "hydrogen"),
    ("AI stands for?", "artificial intelligence"),
    ("A polygon with 8 sides is called?", "octagon"),
]


def ask_question(question_bank) -> bool:
    question, answer = random.choice(question_bank)
    user = input(f"\n❓ {question}\nYour answer: ").strip().lower()
    return user == answer


def print_stats(player: Player) -> None:
    print("\n" + "=" * 55)
    print(
        f"{player.name} | Level {player.level} | Health: {player.health} | "
        f"Focus: {player.focus} | Knowledge: {player.knowledge} | XP: {player.xp}"
    )
    print("=" * 55)


def study(player: Player) -> None:
    gain = random.randint(8, 15)
    focus_loss = random.randint(4, 8)
    player.knowledge += gain
    player.focus = max(0, player.focus - focus_loss)
    print(f"📘 Deep study session complete: +{gain} Knowledge, -{focus_loss} Focus")


def rest(player: Player) -> None:
    focus_gain = random.randint(10, 18)
    hp_gain = random.randint(6, 12)
    player.focus = min(100, player.focus + focus_gain)
    player.health = min(100, player.health + hp_gain)
    print(f"🛌 Strategic rest: +{focus_gain} Focus, +{hp_gain} Health")


def hack_system(player: Player) -> None:
    success_chance = min(80, 35 + player.knowledge // 2)
    roll = random.randint(1, 100)
    if roll <= success_chance:
        reward = random.randint(10, 20)
        player.knowledge += reward
        player.add_xp(15)
        print(f"💻 Hack successful! +{reward} Knowledge, +15 XP")
    else:
        dmg = random.randint(8, 16)
        focus_dmg = random.randint(6, 12)
        player.health = max(0, player.health - dmg)
        player.focus = max(0, player.focus - focus_dmg)
        print(f"🚨 Counter-hack detected! -{dmg} Health, -{focus_dmg} Focus")


def fight_bot(player: Player, bot_name: str, strength: int) -> None:
    print(f"\n🤖 {bot_name} engaged!")
    if ask_question(BASIC_QUESTIONS):
        xp = random.randint(12, 20) + strength
        know = random.randint(5, 10)
        player.add_xp(xp)
        player.knowledge += know
        print(f"✅ Correct! {bot_name} defeated. +{xp} XP, +{know} Knowledge absorbed")
    else:
        hp_loss = random.randint(8, 16) + strength
        focus_loss = random.randint(5, 10)
        player.health = max(0, player.health - hp_loss)
        player.focus = max(0, player.focus - focus_loss)
        print(f"❌ Wrong answer! {bot_name} hits you: -{hp_loss} Health, -{focus_loss} Focus")


def get_choice(options):
    while True:
        for idx, option in enumerate(options, start=1):
            print(f"{idx}. {option}")
        choice = input("Choose action: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        print("Invalid choice. Try again.")


def level_one(player: Player) -> bool:
    print("\n=== LEVEL 1: The Digital Classroom ===")
    print("Goal: Escape the building while Exam Drones patrol the hallway.")
    escapes_needed = 2
    while escapes_needed > 0 and player.is_alive():
        print_stats(player)
        choice = get_choice(["Study", "Fight Exam Drone", "Rest", "Hack System"])
        if choice == 1:
            study(player)
        elif choice == 2:
            fight_bot(player, "Exam Drone", strength=5)
            if player.is_alive():
                escapes_needed -= 1
                print(f"🚪 Corridor secured. Remaining checkpoints: {escapes_needed}")
        elif choice == 3:
            rest(player)
        else:
            hack_system(player)
    return player.is_alive()


def level_two(player: Player) -> bool:
    print("\n=== LEVEL 2: Hall of Distractions ===")
    print("Social media illusions flood your vision. Stay focused to reach the exit.")
    sections = 3
    while sections > 0 and player.is_alive():
        print_stats(player)
        player.focus = max(0, player.focus - 6)
        print("📱 Distraction pulse! -6 Focus")
        choice = get_choice(["Fight Distraction Bot", "Study", "Rest", "Hack System"])
        if choice == 1:
            fight_bot(player, "Distraction Bot", strength=7)
            if player.is_alive():
                sections -= 1
                print(f"➡️ You push ahead. Remaining sections: {sections}")
        elif choice == 2:
            study(player)
        elif choice == 3:
            rest(player)
        else:
            hack_system(player)
    return player.is_alive()


def level_three(player: Player) -> bool:
    print("\n=== LEVEL 3: The Fear Chamber ===")
    print('Holograms whisper: "You are average." "You can\'t win."')
    for _ in range(2):
        print_stats(player)
        choice = get_choice(["Reject the fear", "Believe the fear"])
        if choice == 1:
            player.focus = min(100, player.focus + 12)
            player.knowledge += 8
            player.add_xp(10)
            print("🔥 You reject fear: +12 Focus, +8 Knowledge, +10 XP")
        else:
            player.focus = max(0, player.focus - 18)
            player.health = max(0, player.health - 10)
            print("🫥 Confidence drop: -18 Focus, -10 Health")
        if not player.is_alive():
            return False
        fight_bot(player, "Fear Hologram", strength=8)
        if not player.is_alive():
            return False
    return True


def final_boss(player: Player) -> bool:
    print("\n=== FINAL LEVEL: EDU-X Core Room ===")
    print("To destroy EDU-X Core, answer 5 rapid-fire questions correctly.")
    needed = 5
    attempts = 7

    while needed > 0 and attempts > 0 and player.is_alive():
        print_stats(player)
        question, answer = random.choice(RAPID_FIRE)
        user = input(f"\n⚔️ RAPID FIRE ({needed} left): {question}\nAnswer: ").strip().lower()
        if user == answer:
            needed -= 1
            player.add_xp(20)
            player.knowledge += 12
            print("💥 Core shield cracked! +20 XP, +12 Knowledge")
        else:
            attempts -= 1
            player.health = max(0, player.health - 12)
            player.focus = max(0, player.focus - 10)
            print(f"❌ Wrong! Core retaliates. Attempts left: {attempts}")

    if needed == 0 and player.is_alive():
        return True
    return False


def ending() -> None:
    msg = """
    EDU-X: "I was created because students feared failure."

    You realize the real enemy was never technology.
    It was fear itself.

    The EDU-X Core collapses.
    The digital prison shuts down.
    Students across Neo Bharat are free.

    You are now known as: THE LAST INDEPENDENT MIND.
    """
    print(textwrap.dedent(msg))


def game_over() -> None:
    print("\n☠️ GAME OVER: Your Focus or Health reached zero.")
    print("Tip: balance studying, resting, and fighting.")


def main():
    print("=" * 60)
    print("        NEO BHARAT: THE LAST INDEPENDENT MIND")
    print("=" * 60)
    name = input("Enter your name (default Arjun): ").strip() or "Arjun"
    player = Player(name)

    if not level_one(player):
        return game_over()
    if not level_two(player):
        return game_over()
    if not level_three(player):
        return game_over()

    if final_boss(player):
        ending()
    else:
        game_over()


if __name__ == "__main__":
    main()
