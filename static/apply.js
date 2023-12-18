const movableElement = document.getElementById('apply');

// функция для генерации случайной позиции
function getRandomPosition() {
    const x = Math.floor(Math.random() * window.innerWidth); // случайная позиция по горизонтали
    const y = Math.floor(Math.random() * window.innerHeight); // случайная позиция по вертикали
    return { x, y };
}

// обработчик события наведения курсора
movableElement.addEventListener('mouseover', function() {
    const newPosition = getRandomPosition();
    movableElement.style.left = newPosition.x + 'px'; // устанавливаем новую позицию по горизонтали
    movableElement.style.top = newPosition.y + 'px'; // устанавливаем новую позицию по вертикали
});




