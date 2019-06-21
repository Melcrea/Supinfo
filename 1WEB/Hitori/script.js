var markBoard = [];
var markBoard_c = [];
var clock = 0;
var currentBoard = 0;
var amountBoard = 3;
var sizeBoard = 5;

function resetClock() {
  clock=0;
}

function addTime(time) {
  clock += time;
}

function randomNumber(min, max) {
  return Math.floor((Math.random() * max) + min);
}

function createTable(size) {
  //On génére le tableau html avec du javascript
  var board = document.getElementById("board");

  for (var i = 0; i < size; i++) {
    var boardRows = board.insertRow(-1);
    for (var j = 0; j < size; j++) {
      boardRows.insertCell(j);
    }
  }
}

function newBoard(current, max){
  //Trouve un nouveau tableau
  //Si c'est toujours le meme on continue d'en chercher un nouveau
  level = randomNumber(1, max);
  while (level == current) {
    level = randomNumber(1, max);
  }
  return level
}

function displayNumbers(current) {
  //Lit les fichiers sauvegardés et les transfères dans le tableau html
  var level = [];
  $.get("board/" + current + ".txt", function (txt){
    level = JSON.parse(txt);

    var boardRows = document.getElementById("board").rows;
    for (var i = 0; i < level.length; i++) {
      var boardColumns = boardRows[i].cells;
      for (var j = 0; j < level.length; j++) {
        boardColumns[j].innerHTML = level[i][j];
      }
    }
  });
}

function newEmptyBoard(board, size) {
  //Vide le tableau des cases sélectionnées
  for (var i = 0; i < size; i++) {
    board[i] = [];
    for (var j = 0; j < size; j++) {
      board[i][j] = 0;
    }
  }
}

$('#newB').click(function() {
  currentBoard = newBoard(currentBoard, amountBoard);
  displayNumbers(currentBoard);
  newEmptyBoard(markBoard, sizeBoard);
  $('td').css("background-color", "rgb(200, 200, 200)");
  resetClock();
});

$('#checkB').click(function() {
  var mark = [];
  //Va chercher dans les fichiers le tableau correspondant
  $.get("resolved/" + currentBoard + ".txt", function (txt){
    mark = JSON.parse(txt);
    //... le compare ...
    if (JSON.stringify(markBoard) != JSON.stringify(mark)) {
      //rajoute du temps si c'est faux
      addTime(15);
    } else {
      //alerte le joueur de sa réussite
        alert("Bravo vous avez réussi en " + clock + " secondes");
        currentBoard = newBoard(currentBoard, amountBoard);
      displayNumbers(currentBoard);
      newEmptyBoard(markBoard, sizeBoard);
      $('td').css("background-color", "rgb(200, 200, 200)");
      resetClock();
    }
  });
});

$('#resetB').click(function() {
  //Vide le tableau des cases sélectionnées
  newEmptyBoard(markBoard, sizeBoard);
  //Recolorie toutes les cases avec la couleur d'origine
  $('td').css("background-color", "rgb(200, 200, 200)");
});

$("#board").on("click", "td", function() {
  var rowCell = $(this).parent().index();
  var columnCell = $(this).index();
  //La case n'est pas sélectionnée
  if (markBoard[rowCell][columnCell] == 0) {
    //On définit la case comme sélectionnée
    markBoard[rowCell][columnCell] = 1;
    $(this).css("background-color", "rgb(100, 100, 100)")
  } else {
    //On déselectionne la case sélectionnée
    markBoard[rowCell][columnCell] = 0;
    $(this).css("background-color", "rgb(200, 200, 200)")
  }
});

$("#rules_b").hover(function(){
  //On affiche les règles
  $("#rules_p").css("display", "block");
}, function(){
  //On cache les règles
  $("#rules_p").css("display", "none");
});

$(document).ready(function(){
  createTable(sizeBoard);
  currentBoard = newBoard(currentBoard, amountBoard);
  displayNumbers(currentBoard);
  newEmptyBoard(markBoard, sizeBoard);

  var timer = setInterval(function(){
    //On incrémente le timer
    clock += 1;
    $("#hour").text(Math.floor(clock/3600));
    $("#minute").text(Math.floor((clock%3600)/60));
    $("#second").text(Math.floor((clock%3600)%60));
  }, 1000);
});
