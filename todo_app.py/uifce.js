async function addTask() {
    const taskInput = document.getElementById('taskInput').value;          
    if (!taskInput.trim()) {
        alert('Please enter a task');           // Block which adds a task. Gets the task input from input element with ID. If nothing, asks for user to enter a task. 
        return;
    }
// Sends post request with task input, requesting it in that way. Awaits for a response and takes its data. Displays alert message if its been received.
    const response = await fetch('/api/add_task', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ task: taskInput })
    });

    const result = await response.json();
    alert(result.message);
}

async function removeTask() {
    const taskInput = document.getElementById('taskInput').value;
    if (!taskInput.trim()) {
        alert('Please enter a task');
        return;
    }
// For removing tasks, similar to adding a task as it sends post request with the task input. Then displays message on if it was received. 
// Extracts data through fetching in order to gain the tasks and build the list. 
    const response = await fetch('/api/remove_task', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ task: taskInput })
    });

    const result = await response.json();
    alert(result.message);
}
// Utilizing json formatting in order to use the information and data given between the server and web application. 
async function showTasks() {
    const response = await fetch('/api/show_tasks');
    const result = await response.json();
    if (result.tasks.length === 0) {            // For displaying all of the tasks, use get request and awaits response to get json data. If no tasks, says no tasks. If there are, displays tasks in numbered list how it was made.
        alert('No tasks');
    } else {
        let tasks = '';
        for (let i = 0; i < result.tasks.length; i++) {
            tasks += (i + 1) + '. ' + result.tasks[i] + '\n';
        }
        alert('Tasks:\n' + tasks);
    }
}
