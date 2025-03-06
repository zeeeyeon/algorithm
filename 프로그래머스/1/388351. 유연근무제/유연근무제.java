class Solution {
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int result = 0;

        for (int i = 0; i < schedules.length; i++) {
            int[] dailyLogs = timelogs[i];
            int latestTime = getSchedule(schedules[i]);

            int currentDay = startday;
            int workDays = 0;

            for (int logTime : dailyLogs) {
                if (currentDay % 7 == 0 || currentDay % 7 == 6) {  
                    currentDay++;
                    continue;
                }
                
                if (logTime <= latestTime) {  
                    workDays++;
                }

                currentDay++;
            }

            if (workDays == 5) {  
                result++;
            }
        }

        return result;
    }
    
    private int getSchedule(int schedule) {
        schedule += 10; 

        int hours = schedule / 100;
        int minutes = schedule % 100;

        if (minutes >= 60) {
            hours++;
            minutes -= 60;
        }

        return (hours * 100) + minutes;
    }
}