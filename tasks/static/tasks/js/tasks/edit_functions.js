function edit_tasks_click_events() {
    $('.edit_task').unbind('click').click(function(){
        let task_id = $(this).attr('data-task-id');
        console.log("Edit for:" + task_id);
        alert(tasks[task_id]);

    });
}

$(document).ready(function(){
    // add click event to each edit_task element
    edit_tasks_click_events();
});