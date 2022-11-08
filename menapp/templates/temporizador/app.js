window.onload = function() {
    function format(Hour, Minute, Second) {
        if (Second < 10) {
            secondString = "0" + Second;
        } else {
            secondString = Second;
        }

        if (Minute < 10) {
            minuteString = "0" + Minute;
        } else {
            minuteString = Minute;
        }

        if (Hour < 10) {
            hourString = "0" + Hour;
        } else {
            hourString = Hour;
        }
        return hourString + ":" + minuteString + ":" + secondString;
    }

    function changeStatus(aimStatus) {
        if (aimStatus == 1) {
            for (var i = 0; i < initial.length; i++) {
                initial[i].style.display = "inline";
            }
            hint.style.display = "none";
            clear.style.display = "none";
            pause.style.display = "none";
            restart.style.display = "none";
            resume.style.display = "none";
        } else if (aimStatus == 2 || aimStatus == 3) {
            for (var i = 0; i < initial.length; i++) {
                initial[i].style.display = "none";
            }
            hint.style.display = "inline";
            clear.style.display = "inline";
            pause.style.display = "inline";
            restart.style.display = "inline";
            resume.style.display = "none";

            if (aimStatus == 2) {
                // up timing
                hint.innerText = "El tiempo corre";
                clear.innerText = "Vaciar el tiempo";
            } else if (aimStatus == 3) {
                // down timing
                recordHour = parseInt(recordMilliSecond / 3600000);
                recordMinute = parseInt((recordMilliSecond % 3600000) / 60000);
                recordSecond = parseInt((recordMilliSecond % 60000) / 1000);
                hint.innerText = "Contando hacia atrás" + format(recordHour, recordMinute, recordSecond);
                clear.innerText = "Vaciar la cuenta atrás";
            }
        } else if (aimStatus == 4 || aimStatus == 5) {
            for (var i = 0; i < initial.length; i++) {
                initial[i].style.display = "none";
            }
            hint.style.display = "inline";
            clear.style.display = "inline";
            pause.style.display = "none";
            restart.style.display = "inline";
            resume.style.display = "inline";

            if (aimStatus == 4) {
                // up pausing
                hint.innerText = "Pausar el tiempo";
                clear.innerText = "Vaciar el tiempo";
            } else if (aimStatus == 5) {
                // down pausing
                recordHour = parseInt(recordMilliSecond / 3600000);
                recordMinute = parseInt((recordMilliSecond % 3600000) / 60000);
                recordSecond = parseInt((recordMilliSecond % 60000) / 1000);
                hint.innerText = "Pausar cuenta regresiva" + format(recordHour, recordMinute, recordSecond);
                clear.innerText = "Vaciar la cuenta atrás";
            }
        } else if (aimStatus == 6) {
            for (var i = 0; i < initial.length; i++) {
                initial[i].style.display = "none";
            }
            hint.style.display = "inline";
            clear.style.display = "inline";
            pause.style.display = "none";
            restart.style.display = "inline";
            resume.style.display = "none";

            recordHour = parseInt(recordMilliSecond / 3600000);
            recordMinute = parseInt((recordMilliSecond % 3600000) / 60000);
            recordSecond = parseInt((recordMilliSecond % 60000) / 1000);
            hint.innerText = "Cuenta regresiva" + format(recordHour, recordMinute, recordSecond) + " encima";
        }
    }

    function CountUp() {
        MilliSecond += 50;
        Hour = parseInt(MilliSecond / 3600000);
        Minute = parseInt((MilliSecond % 3600000) / 60000);
        Second = parseInt((MilliSecond % 60000) / 1000);

        time.innerText = format(Hour, Minute, Second);
    }

    function CountDown() {
        MilliSecond -= 50;
        Hour = parseInt(MilliSecond / 3600000);
        Minute = parseInt((MilliSecond % 3600000) / 60000);
        Second = parseInt((MilliSecond % 60000) / 1000);
        if (MilliSecond <= 0) {
            clearInterval(timer);
            changeStatus(6);
        }
        time.innerText = format(Hour, Minute, Second);
    }

    var hour = document.getElementById("hour"),
        minute = document.getElementById("minute"),
        second = document.getElementById("second"),
        initial = document.getElementsByClassName("initial"),
        countup = document.getElementById("countup"),
        countdown = document.getElementById("countdown"),
        clear = document.getElementById("clear"),
        pause = document.getElementById("pause"),
        restart = document.getElementById("restart"),
        resume = document.getElementById("resume"),
        time = document.getElementById("time"),
        timer = null,
        Hour = 0,
        Minute = 0,
        Second = 0,
        MilliSecond = 0,
        recordMilliSecond = 0;
        hourString = "",
        minuteString = "",
        secondString = "",
        // Status---1: before start; 2: up timing; 3: down timing; 4: up pausing;
        // 5: down pausing; 6: down finished;
        status = 1;


    changeStatus(status);

    countup.onclick = function() {
        status = 2;
        MilliSecond = 0;
        changeStatus(status);
        timer = setInterval(CountUp, 50);
    }


    countdown.onclick = function() {
        status = 3;
        Hour = hour.value;
        if (minute.value > 59) {
            Minute = 59;
        } else {
            Minute = minute.value;
        }
        if (second.value > 59) {
            Second = 59;
        } else {
            Second = second.value;
        }

        hour.value = null;
        minute.value = null;
        second.value = null;

        MilliSecond = Hour * 3600000 + Minute * 60000 + Second * 1000;
        recordMilliSecond = MilliSecond;
        changeStatus(status);

        timer = setInterval(CountDown, 50);
    }

    clear.onclick = function() {
        status = 1;
        changeStatus(status);
        clearInterval(timer);
        time.innerText = format(0, 0, 0);
    }

    pause.onclick = function() {
        if (status == 2) {
            // Now count up
            status = 4;
            changeStatus(status);
            clearInterval(timer);
        } else if (status == 3) {
            // now count down
            status = 5;
            changeStatus(status);
            clearInterval(timer);
        }
    }

    restart.onclick = function() {
        if (status == 2 || status == 4) {
            status = 2;
            MilliSecond = 0;
            changeStatus(status);
            clearInterval(timer);
            timer = setInterval(CountUp, 50);
        } else if (status = 3 || status == 5 || status == 6) {
            status = 3;
            MilliSecond = recordMilliSecond;
            changeStatus(status);
            clearInterval(timer);
            timer = setInterval(CountDown, 50);
        }
    }

    resume.onclick = function() {
        if (status == 4) {
            status = 2;
            changeStatus(status);
            timer = setInterval(CountUp, 50);
        } else if (status = 5) {
            status = 3;
            changeStatus(status);
            timer = setInterval(CountDown, 50);
        }
    }

    document.onkeydown = function(event) {
        var e = event || window.event || arguments.callee.caller.arguments[0];
        if (e && e.keyCode == 13) {
            // Enter
            if (status == 1) {
                // before start
                status = 2;
                MilliSecond = 0;
                changeStatus(status);
                timer = setInterval(CountUp, 50);
            }
        }

        if (e && e.keyCode == 32) {
            // space
            if (status == 2) {
                // Now count up
                status = 4;
                changeStatus(status);
                clearInterval(timer);
            } else if (status == 3) {
                // now count down
                status = 5;
                changeStatus(status);
                clearInterval(timer);
            } else if (status == 4) {
                status = 2;
                changeStatus(status);
                timer = setInterval(CountUp, 50);
            } else if (status == 5) {
                status = 3;
                changeStatus(status);
                timer = setInterval(CountDown, 50);
            }
        }
    };
}
