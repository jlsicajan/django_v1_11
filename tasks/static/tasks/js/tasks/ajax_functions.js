function db_delete_task(callback, task_id) {
    $.ajax({
        type: 'POST',
        url: 'ajax/delete_task/',
        data: {
            'task_id': task_id,
            csrfmiddlewaretoken: csfr_token_value
        },
        success: function (data) {
            console.log("done!");
            console.log(data);
            if(data){
                callback(task_id);
                alert('Taks deleted');
            }else{
                alert('The task was no deleted');
            }
        }
    });
    // $.ajaxSetup({
    //     data: {csrfmiddlewaretoken: csfr_token_value},
    // });
    // $.post("ajax/delete_task/", {
    //     task_id: task_id
    // }, function (data) {
    //     console.log("done!");
    //     console.log(data);
    //     callback(task_id);
    // });

}
