$(document).ready(function () {
    $('.task_priority').on('change', function () {
        let task_id = $(this).attr('data-task-id');
        db_change_priority_task(task_id, this.value);

    })
});