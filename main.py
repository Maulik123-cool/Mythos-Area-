import random
import time

# Mythical creatures with health and attack ranges
creatures = {
    "Hydra": {"health": 100, "attack": (10, 25)},
    "Phoenix": {"health": 90, "attack": (12, 22)},
    "Minotaur": {"health": 110, "attack": (8, 20)},
    "Kraken": {"health": 95, "attack": (15, 18)},
    "Griffin": {"health": 85, "attack": (14, 26)}
}

def print_pause(text, delay=1):
    print(text)
    time.sleep(delay)

def choose_creature():
    print("Choose your mythic warrior:")
    for i, name in enumerate(creatures.keys(), start=1):
        print(f"{i}. {name}")
    while True:
        try:
            choice = int(input("Enter number: "))
            creature_name = list(creatures.keys())[choice - 1]
            return creature_name
        except (ValueError, IndexError):
            print("⚠️ Invalid choice. Try again.")

def battle(player, enemy):
    print_pause(f"\n🔥 Battle begins: {player} vs {enemy}!\n")

    player_health = creatures[player]["health"]
    enemy_health = creatures[enemy]["health"]

    while player_health > 0 and enemy_health > 0:
        # Player attacks
        player_damage = random.randint(*creatures[player]["attack"])
        enemy_health -= player_damage
        print_pause(f"{player} attacks {enemy} for {player_damage} damage!")

        if enemy_health <= 0:
            break

        # Enemy attacks
        enemy_damage = random.randint(*creatures[enemy]["attack"])
        player_health -= enemy_damage
        print_pause(f"{enemy} strikes back for {enemy_damage} damage!")

        # Show health bars
        print_pause(f"{player} HP: {player_health} | {enemy} HP: {enemy_health}\n", 0.5)

    if player_health > 0:
        print_pause(f"🏆 {player} wins the battle!")
    else:
        print_pause(f"💀 {enemy} defeats you. Better luck next time!")

def play_game():
    print("⚔️ Welcome to Mythos Arena!")
    player = choose_creature()
    enemy = random.choice([c for c in creatures if c != player])
    battle(player, enemy)

    again = input("\nDo you want to battle again? (y/n): ").strip().lower()
    if again == "y":
        print()
        play_game()
    else:
        print("Thanks for fighting in the Mythos Arena!")

if __name__ == "__main__":
    play_game()
