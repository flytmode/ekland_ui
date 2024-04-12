

@main_bp.route("/airport_data_fetch", methods=["GET"])
def airport_data_fetch():
    try:
        
        timestream_client = boto3.client('timestream-query')

        # Define the measurements you want to query
        measure_names = ["QFE_Avg", "QNH_Avg", "WSpd_Avg", "WDir_Avg", "BPress_Avg", "AirTemp_Avg", "RH", "DewPointTemp_Avg", "Rain_1h_RunTot", "Rain_12h_RunTot", "SkyVUE_FirstLayerCloudAmount", "SkyVUE_FirstLayerCloudHeight", "SkyVUE_SecondLayerCloudAmount", "SkyVUE_SecondLayerCloudHeight", "SkyVUE_ThirdLayerCloudAmount", "SkyVUE_ThirdLayerCloudHeight"]

        # Construct the query string
        query_string = 'SELECT * FROM "mqtt_dashboard"."CSAf_southafrica_Limpopo_SHA_Aviation_SHA_AWOS_6240_data_cr1000x_56192_Table2m" WHERE measure_name IN ({}) ORDER BY time DESC LIMIT 16'.format(', '.join([f"'{name}'" for name in measure_names]))

        response = timestream_client.query(QueryString=query_string)

        # Extract and format the results
        timestream_results = []
        for row in response['Rows']:
            data = [data['ScalarValue'] for data in row['Data'] if data.get('ScalarValue')]
            timestream_results.append(data)

        # Return the extracted data
        return jsonify(timestream_results)

    except Exception as e:
        return jsonify({'error': str(e)})
    


    
@main_bp.route("/airport_data_fetch_10m", methods=["GET"])
def airport_data_fetch_10m():
    try:
        
        timestream_client = boto3.client('timestream-query')

        # Define the measurements you want to query
        measure_names = ["WSpd_Avg", "WDir_Avg", "AirTemp_Avg", "QFE_Avg", "WSpd_Max"]

        # Construct the query string
        query_string = 'SELECT * FROM "mqtt_dashboard"."CSAf_southafrica_Limpopo_SHA_Aviation_SHA_AWOS_6240_data_cr1000x_56192" WHERE measure_name IN ({}) ORDER BY time DESC LIMIT 28'.format(', '.join([f"'{name}'" for name in measure_names]))

        response = timestream_client.query(QueryString=query_string)

        # Extract and format the results
        timestream_results = []
        for row in response['Rows']:
            data = [data['ScalarValue'] for data in row['Data'] if data.get('ScalarValue')]
            timestream_results.append(data)

        # Return the extracted data
        return jsonify(timestream_results)

    except Exception as e:
        return jsonify({'error': str(e)})
    

    
@main_bp.route("/airport_ui")
@login_required
def airport_ui():
    try:
        # Get the name of the logged-in user
        user_name = current_user.name if current_user.is_authenticated else None

        # Pass the logged-in user's name to the template
        return render_template("wind-barb.html", user_name=user_name)
    
    except Exception as e:
            return jsonify({'error': str(e)})
    
@main_bp.route("/ekland_ui")

def ekland_ui():
    try:
        # Get the name of the logged-in user
        user_name = current_user.name if current_user.is_authenticated else None

        # Pass the logged-in user's name to the template
        return render_template("layout.html", user_name=user_name)
    
    except Exception as e:
            return jsonify({'error': str(e)})
    
    
