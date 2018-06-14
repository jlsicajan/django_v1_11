function remove_task_html(task_id) {
    $('tr[data-task-id=' + task_id + ']').remove();
}

function delete_tasks_click_event() {
    $('.delete_task').unbind('click').click(function () {
        let task_id = $(this).attr('data-task-id');
        db_delete_task(remove_task_html, task_id);
    });
}

$(document).ready(function () {
    // add click event to each delete_task element
    delete_tasks_click_event();

});