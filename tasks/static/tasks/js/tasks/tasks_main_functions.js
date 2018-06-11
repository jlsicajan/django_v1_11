function delete_task(callback, task_id) {
    $('tr[data-task-id=' + task_id + ']').remove();
}

$(document).ready(function () {
    $('.delete_task').unbind('click').click(function () {
        let task_id = $(this).attr('data-task-id');
        delete_task(function () {
        }, task_id);
    });
});