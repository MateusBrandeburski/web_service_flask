var interval;
var minutes = 25;
var seconds = 0;

function startTimer() {
  interval = setInterval(function() {
    var timerElement = document.getElementById('timer');
    timerElement.innerHTML = minutes + ':' + (seconds < 10 ? '0' : '') + seconds;
    if (--seconds < 0) {
      seconds = 59;
      if (--minutes < 0) {
        clearInterval(interval);
        alert('Tempo acabou!');
      }
    }
  }, 1000);
}

function pauseTimer() {
  clearInterval(interval);
}
  

