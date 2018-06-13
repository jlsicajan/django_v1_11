function delete_task(callback, task_id) {
    $('tr[data-task-id=' + task_id + ']').remove();
}

var task_selected = '';

function assign_task_to_user_clicks(callback) {

    $('.assign-task-to-user').unbind('click').click(function () {
        let user_id = $(this).attr('data-user-id');
        alert("task_id " + task_selected + " assigned to user_id: " + user_id);
        $(this).removeClass('btn-outline-success assign-task-to-user').addClass('btn-outline-danger unassign-task-to-user');
        $(this).text('Unassign');
        unassign_task_to_user_clicks(function () {
            console.log('done');
        })
    });
    callback();
}

function unassign_task_to_user_clicks(callback) {
    $('.unassign-task-to-user').unbind('click').click(function () {
        let user_id = $(this).attr('data-user-id');
        if (confirm("Unassign task?")) {
            $(this).removeClass('btn-outline-danger disabled unassign-task-to-user').addClass('btn-outline-success assign-task-to-user');
            $(this).text('Assign');
            assign_task_to_user_clicks(function(){console.log('done!');});
            alert("Task_id " + task_selected + "unassigned from the user " + user_id);
        }
    });
    callback();
}

$(document).ready(function () {
    $('.delete_task').unbind('click').click(function () {
        let task_id = $(this).attr('data-task-id');
        delete_task(function () {
        }, task_id);
    });

    $('.assign_to_user').unbind('click').click(function () {
        let task_id = $(this).attr('data-task-id');
        task_selected = task_id;
        $('#selectUser').modal("show");
        console.log("tasks selected");
        console.log(task_id);
    });
    assign_task_to_user_clicks(function () {
        console.log('click added');
    });
});