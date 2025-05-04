
$("#id_foodname, #id_quantity").change(function () {
    var nutritionId = $("#id_foodname").val();
    var url = "/api/nutrition-metrics/food/details";
    var qty = $("#id_quantity").val();
    if(!qty || qty=="") {
        qty = 0;
    }

    $.ajax({
      url: url,
      data: {
        'nutritionId': nutritionId
      },
      success: function (data) {
        console.log(data);
        $("#id_calories").val(data.calories * qty);
        $("#id_carbs").val(data.carbs * qty);
        $("#id_fat").val(data.fat * qty);
        $("#id_sugar").val(data.sugar * qty);
        $("#id_protein").val(data.protein * qty);

        $("#id_calories").parent().addClass("is-filled");
        $("#id_carbs").parent().addClass("is-filled");
        $("#id_fat").parent().addClass("is-filled");
        $("#id_sugar").parent().addClass("is-filled");
        $("#id_protein").parent().addClass("is-filled");
      }
    });

});


function showHideLossGainTable() {
    var weightLossOrGain = $("#id_weightLossOrGain").val();
    console.log("id_weightLossOrGain", weightLossOrGain)


    if(weightLossOrGain === "True") {
        // $('#weightLoss').addClass("d-block");
        $('#weightLoss').removeClass("d-none");

        $('#weightGain').addClass("d-none");
        // $('#weightGain').removeClass("d-block");
    } else if(weightLossOrGain === "False") {

        // $('#weightGain').addClass("d-block");
        $('#weightGain').removeClass("d-none");

        $('#weightLoss').addClass("d-none");
        // $('#weightLoss').removeClass("d-block");

    } else {
        $('#weightLoss').addClass("d-none");
        $('#weightGain').addClass("d-none");
    }
}


$(document).ready(function() {

    $("select").change(function(){
        var value = $(this).val();
        console.log("Select value: ", value)
        if(value != '') {
            $(this).parent().addClass("is-filled");
        } else {
            $(this).parent().removeClass("is-filled");
        }
    });

    $("#id_weightLossOrGain").change(function () {
        showHideLossGainTable();
    });

    showHideLossGainTable();

  });

  