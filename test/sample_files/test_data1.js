// greetings.js
// A simple program to greet users

// Function to return a greeting message
function greet(name) {
    if (!name) {
        return "Hello, Stranger!";
    }
    return "Hello, " + name + "!";
}

// Example usage
console.log(greet("Alice"));
console.log(greet());  // no name passed