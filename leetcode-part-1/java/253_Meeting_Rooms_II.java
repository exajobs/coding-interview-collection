/**
 * Definition for an interval. public class Interval { int start; int end; Interval() { start = 0;
 * end = 0; } Interval(int s, int e) { start = s; end = e; } }
 */
class Solution {

 /* public int minMeetingRooms(Interval[] intervals) {

    // Check for the base case. If there are no intervals, return 0
    if (intervals.length == 0) {
      return 0;
    }
    // Min heap
    PriorityQueue<Integer> allocator =
        new PriorityQueue<Integer>(
            intervals.length,
            new Comparator<Integer>() {
              public int compare(Integer a, Integer b) {
                return a - b;
              }
            });

    // Sort the intervals by start time
    Arrays.sort(
        intervals,
        new Comparator<Interval>() {
          public int compare(Interval a, Interval b) {
            return a.start - b.start;
          }
        });
    // Add the first meeting
    allocator.add(intervals[0].end);

    // Iterate over remaining intervals
    for (int i = 1; i < intervals.length; i++) {
      // If the room due to free up the earliest is free, assign that room to this meeting.
      if (intervals[i].start >= allocator.peek()) {
        allocator.poll();
      }
      // If a new room is to be assigned, then also we add to the heap,
      // If an old room is allocated, then also we have to add to the heap with updated end time.
      allocator.add(intervals[i].end);
    }
    // The size of the heap tells us the minimum rooms required for all the meetings.
    return allocator.size();
  }*/

  public int minMeetingRooms(Interval[] intervals) {
    int ans = 0, curr = 0;
    List<TimePoint> timeline = new ArrayList<>();
    for (Interval interval: intervals) {
      timeline.add(new TimePoint(interval.start, 1));
      timeline.add(new TimePoint(interval.end, -1));
    }
    timeline.sort(new Comparator<TimePoint>() {
          public int compare(TimePoint a, TimePoint b) {
            if (a.time != b.time) return a.time - b.time;
            else return a.room - b.room;
          }
        });
    for (TimePoint t: timeline) {
      curr += t.room;
      if (curr >= ans) ans = curr;
    }
    return ans;
  }  

  private class TimePoint {
    int time;
    int room;

    TimePoint(int time, int room) {
      this.time = time;
      this.room = room;
    }
  }
}
