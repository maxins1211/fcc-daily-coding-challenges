function countBusinessDays(start, end) {
    const startDate = new Date(start)
    const endDate = new Date(end)
    const millisecondsPerDay = 1000 * 60 * 60 * 24;
    const totalDay = (endDate - startDate) / millisecondsPerDay
    let today = startDate.getDay() // 0 - 6 => 5 & 6 are weekends
    let totalWeekdays = 0;
    for (let i = 0; i <= totalDay; i++) {
        if (today > 6) {
            today = 0;
        }
        if (today !== 5 && today !== 6) {
            totalWeekdays++;
        }
        today++;
    }
    return totalWeekdays;
}