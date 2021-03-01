window.onload = function () {
    const clockBox = document.getElementById("clock");
    const dateBox = document.getElementById("date")

    function clock() {
        const date = new Date();

        let year = date.getFullYear();
        let month = date.getMonth();
        let day = date.getDay();

        let hours = date.getHours();
        let minutes = date.getMinutes();
        let seconds = date.getSeconds();

        if (hours < 10) hours = "0" + minutes;
        if (minutes < 10) minutes = "0" + minutes;
        if (seconds < 10) seconds = "0" + seconds;

        dateBox.innerText = `${year}년 ${month}월 ${day}일`;
        clockBox.innerText = `${hours} : ${minutes} : ${seconds}`;
    }

    clock();
    setInterval(clock, 1000);
}