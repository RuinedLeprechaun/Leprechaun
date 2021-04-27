var restart= document.querySelector('#b');
var squares= document.querySelectorAll('td');
function ClearBoard() {
  for (var i = 0; i < squares.length; i++) {
    squares[i].textContent=' ';
  }
}
restart.addEventListener('click',ClearBoard);
var player=1;
function changeMarker() {
  if (player===1 && this.textContent===' ') {
    this.textContent ="X";
    player=2;
  } else if (player===2 && this.textContent===' ') {
    this.textContent ="O";
    player=1;
  }
}
for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener('click',changeMarker);
}
