# Calculate Minute Hand Position: Minutes * 6
# Calculate Hour Hand Position: (Hours*30) + (Minutes*0.5)
# Find the Difference: Subtract the smaller value from the larger value.

class Solution:
    def getAngle(self, s: str) -> float:
        hours = int(s[0:2])
        minutes = int(s[3:])
        """
            hours -> 06 
            minutes -> 00
            
            so the clock has circle 360º
            Minute Hand
                Full circle = 360°
                It completes in 60 minutes
                So,
                    In 1 minute → moves 360 / 60 = 6°
            minute_angle ->  00 * 6  = 0;
            
            hours_angle -> 06%12 = 6 * 30 => 180 + 0;
            angle -> 180 - 0 => 180
            min(180,360-180) => 180
            
            2. 
            hours -> 03 
            minutes -> 15
            minute_angle -> 15*6 = 90
            hours_angle -> 3%12 = 3 * 30 => 90 + (15*0.5) => 7.5 ==> 10 + 7.5 = 97.5
            angle = abs(97.5 - 90) => 7.5
            min(7.5,360-7.5) =>  7.5
        """
        minute_angle = minutes *6;
        hours_angle = (hours%12 ) * 30 + (minutes*0.5);
        angle = abs(hours_angle - minute_angle);
        return min(angle, 360 - angle);
obj = Solution();
print(obj.getAngle("06:00"));
print(obj.getAngle("03:15"));
print(obj.getAngle("12:00"));
