function createGrid(rows, cols) {
    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            const cell = document.createElement('div');
            cell.classList.add('grid-cell');
            grid.appendChild(cell);
        }
    }
}

createGrid(64, 40)
const colors = ['maroon', 'red', 'coral', 'darksalmon', 'deeppink', 'fuchsia', 'purple', 'crimson', 'burlywood', 'cadetblue', 'darkcyan', 'lightblue', 'blue', 'chartreuse', 'seagreen', 'darkgray', 'darkgreen', 'forestgreen', 'lightgreen', 'greenyellow', 'gold']
function createColorPad(colors) {
    for (let i = 0; i < 21; i++) {
        const color = document.createElement('div');
        color.classList.add('color');
        color.style.backgroundColor = colors[i];
        colorBar.appendChild(color);
    }
}

createColorPad(colors)

let color = 'white';
let isMouseDown;

const getColor = (event) => {
    if (event.type === 'click' && event.target.matches('.color')) {
        const computedStyle = getComputedStyle(event.target);
        color = computedStyle.backgroundColor;
    };
};

const painting = (event) => {
        isMouseDown = true;
        event.target.style.backgroundColor = color;

    grid.addEventListener('mouseup', () => {
        isMouseDown = false;
    });

    event.currentTarget.addEventListener('mouseover', (e) => {
        if (isMouseDown ) e.target.style.backgroundColor = color;
    });
};

const clearGrid = () => {
    document.querySelectorAll('.grid-cell').forEach((cell) => { cell.style.backgroundColor = 'white' });
};

colorBar.addEventListener('click', getColor);
grid.addEventListener('mousedown', painting);
clear.addEventListener('click', clearGrid);