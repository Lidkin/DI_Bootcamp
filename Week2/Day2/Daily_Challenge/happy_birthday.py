from datetime import datetime

def cake():
    try:
        while True:
            user_input = input('Hi! When did you born? Please use YYYY-MM-DD format.')
            user_date = datetime.strptime(user_input, "%Y-%m-%d").date()
            age = datetime.now().date().year-user_date.year
            age_candels_layers = age//10
            if age - age_candels_layers != 0:
                first_layer_candels = round(age%10)
                even_glaze = int((10-first_layer_candels)/2) if first_layer_candels % 2 == 0 else int(round((10-first_layer_candels)/2))
                glaze = even_glaze - 1
                print('    ','_'*(glaze),'i'*first_layer_candels,'_'*glaze) if first_layer_candels % 2 == 0 else print('    ','_'*(glaze+1),'i'*first_layer_candels,'_'*glaze)
            for i in range(age_candels_layers):
                print('    ','i'*10)
            print('    ============')
            print('   | :H:a:p:p:y: |')
            print(' __|_____________|__')
            print('|^^^^^^^^^^^^^^^^^^^^|')
            print('|  B:i:r:t:h:d:a:y!  |')
            print('|                    |')
            print('~~~~~~~~~~~~~~~~~~~~~~') 
            break           
    except Exception:
        print('Wrong date format')

cake()