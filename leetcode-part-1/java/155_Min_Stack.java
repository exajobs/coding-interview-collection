import java.util.ArrayList;
import java.util.List;

/* class MinStack {
    private Stack<Integer> stack;
    private Stack<Integer> minStack;
    public MinStack() {
        stack = new Stack<>();
        minStack = new Stack<>();
    }
    
    public void push(int x) {
        stack.push(x);
        if (minStack.size() == 0 || x <= minStack.peek()) minStack.push(x);
    }
    
    public void pop() {
        if (stack.size() > 0) {
            int curr = stack.pop();
            if (minStack.size() > 0 && curr == minStack.peek()) minStack.pop();
        }
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        if (minStack.size() > 0) 
            return minStack.peek();
        else
            return stack.peek();
    }
} */

class MinStack {
    private Stack<Integer> stack;
    private Stack<Integer> minStack;
    public MinStack() {
        stack = new Stack<>();
        minStack = new Stack<>();
    }
    
    public void push(int x) {
        stack.push(x);
        if (minStack.size() == 0 || x <= minStack.peek()) minStack.push(x);
        else minStack.push(minStack.peek());
    }
    
    public void pop() {
        stack.pop();
        minStack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
