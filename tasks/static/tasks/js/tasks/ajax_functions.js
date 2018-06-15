function db_delete_task(callback, task_id) {
    $.ajax({
        type: 'POST',
        url: '/tasks/ajax/delete_task/',
        data: {
            'task_id': task_id,
            csrfmiddlewaretoken: csfr_token_value
        },
        success: function (data) {
            console.log("done!");
            console.log(data);
            if (data) {
                callback(task_id);
                alert('Task deleted');
            } else {
                alert('The task was no deleted');
            }
        }
    });
}

function db_change_priority_task(task_id, priority_id) {
    $.ajax({
        type: 'POST',
        url: '/tasks/ajax/change_priority_task/',
        data: {
            'task_id': task_id,
            'priority_id': priority_id,
            csrfmiddlewaretoken: csfr_token_value
        },
        success: function (data) {
            console.log("done!");
            console.log(data);
            if (data) {
                alert('Task updated');
            } else {
                alert('The task was not updated');
            }
        }
    });
}

