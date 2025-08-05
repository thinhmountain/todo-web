import React from 'react';

function TaskList({ tasks }) {
  return (
    <ul>
      {tasks.map(task => (
        <li key={task.id}>
          {task.title} - {task.completed ? 'Done' : 'Not done'} - Deadline: {task.deadline}
        </li>
      ))}
    </ul>
  );
}

export default TaskList;
