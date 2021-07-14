timerID = setInterval('clock()',500); //0.5秒毎にclock()を実行

function clock() {
document.getElementById("datetime").innerHTML = getNow();
}

function getNow() {
function set2fig(num) {
    // 桁数が1桁だったら先頭に0を加えて2桁に調整する
    var ret;
    if( num < 10 ) { ret = "0" + num; }
    else { ret = num; }
    return ret;
}
var now = new Date();
var year = now.getFullYear();
var mon = now.getMonth()+1; //１を足す
var day = now.getDate();
var you = now.getDay(); //曜日(0～6=日～土)
var hour = set2fig(now.getHours());
var min = set2fig(now.getMinutes());
var sec = set2fig(now.getSeconds());
var youbi = new Array("日","月","火","水","木","金","土");
//出力用
var s = year + "年" + mon + "月" + day + "日" + "（" + youbi[you] + "）" + hour + ":" + min + ":" + sec + ""; 
return s;
}