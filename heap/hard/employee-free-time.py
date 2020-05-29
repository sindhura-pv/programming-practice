class Solution:
    def employeeFreeTime(self, schedule):

        arr = []
        for employee in schedule:
            arr += [interval for interval in employee]

        arr.sort(key=lambda x: x.start)

        free_time = []

        end = arr[0].end

        for i in range(1, len(arr)):

            if end < arr[i].start:
                free_time.append(Interval(end, arr[i].start))
                end = arr[i].end

            elif arr[i].end > end:
                end = arr[i].end

        return free_time