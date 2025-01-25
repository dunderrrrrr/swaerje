
function leftPad(val) {
    return val < 10 ? '0' + String(val) : val;
}

function timer_text(start, current) {
    let h="00", m="00", s="00";
    const diff = current - start;
    // seconds
    if(diff > 1000) {
        s = Math.floor(diff / 1000);
        s = s > 60 ? s % 60 : s;
        s = leftPad(s);
    }
    // minutes
    if(diff > 60000) {
        m = Math.floor(diff/60000);
        m = m > 60 ? m % 60 : leftPad(m);
    }

    return `${m}:${s}`;
}
