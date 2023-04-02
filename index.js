// PEGAR OS ELEMENTOS DO HTML

const TEXT_INPUT = document.getElementById("input-color");
const CHANGE_BTN = document.getElementById("change-btn");
const SQUARE = document.getElementById("square");

// FUNÇÃO PRA MUDAR A COR DO QUADRADO

const changeColor = () => {
	// adiciona o valor do input em uma nova variável
	let colorSelected = TEXT_INPUT.value;
	// limpa o value do input
	TEXT_INPUT.value = "";
	// muda a cor do quadrado
	SQUARE.style.backgroundColor = colorSelected;
};

CHANGE_BTN.addEventListener("click", changeColor);

// USAR O 'ENTER' PRA MUDAR A COR

const changeWithEnter = (e) => {
	if (e.keyCode === 13) {
		changeColor();
	}
};

TEXT_INPUT.addEventListener("keydown", changeWithEnter);
