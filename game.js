const creatures = {
  Hydra: { health: 100, attack: [10, 25] },
  Phoenix: { health: 90, attack: [12, 22] },
  Minotaur: { health: 110, attack: [8, 20] },
  Kraken: { health: 95, attack: [15, 18] },
  Griffin: { health: 85, attack: [14, 26] }
};

let player = null;
let enemy = null;
let playerHP = 0;
let enemyHP = 0;

const creatureButtons = document.getElementById("creature-buttons");
const status = document.getElementById("status");
const battleSection = document.getElementById("battle");
const attackBtn = document.getElementById("attackBtn");

// Create buttons for each creature
for (let name in creatures) {
  const btn = document.createElement("button");
  btn.textContent = name;
  btn.onclick = () => startGame(name);
  creatureButtons.appendChild(btn);
}

function startGame(selected) {
  player = selected;
  enemy = Object.keys(creatures).filter(c => c !== player)[Math.floor(Math.random() * 4)];

  playerHP = creatures[player].health;
  enemyHP = creatures[enemy].health;

  document.getElementById("selection").style.display = "none";
  battleSection.style.display = "block";
  updateStatus(`${player} vs ${enemy} — let the battle begin!`);
}

function updateStatus(text) {
  status.textContent = text;
}

attackBtn.onclick = () => {
  if (playerHP <= 0 || enemyHP <= 0) return;

  const playerDmg = random(creatures[player].attack);
  enemyHP -= playerDmg;

  let battleText = `${player} hits ${enemy} for ${playerDmg} damage!`;

  if (enemyHP > 0) {
    const enemyDmg = random(creatures[enemy].attack);
    playerHP -= enemyDmg;
    battleText += `\n${enemy} counters with ${enemyDmg} damage!`;
  }

  if (playerHP <= 0 && enemyHP <= 0) {
    updateStatus(`${battleText}\nIt's a draw!`);
    attackBtn.disabled = true;
  } else if (enemyHP <= 0) {
    updateStatus(`${battleText}\n🏆 ${player} wins!`);
    attackBtn.disabled = true;
  } else if (playerHP <= 0) {
    updateStatus(`${battleText}\n💀 ${enemy} wins!`);
    attackBtn.disabled = true;
  } else {
    updateStatus(`${battleText}\n${player} HP: ${playerHP} | ${enemy} HP: ${enemyHP}`);
  }
};

function random([min, max]) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}
