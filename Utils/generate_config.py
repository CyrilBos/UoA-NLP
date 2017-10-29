import os, configparser 

def GenerateConfig(configfile_name = "config.ini"):

    # Check if there is already a configurtion file
    if not os.path.isfile(configfile_name):
        # Create the configuration file as it doesn't exist yet
        cfgfile = open(configfile_name, 'w')

        # Add content to the file
        Config = configparser.ConfigParser()
        Config.add_section('data')
        Config.set('data', 'data_source', 'xero')
        Config.set('data', 'training_data', 'Business')

        Config.add_section('printing')
        Config.set('printing','print_to_csv', '1')
        Config.set('printing','print_to_file', '0')

        Config.add_section('other')
        Config.set('other', 'preprocess', '0')
        Config.set('other', 'n_features', '20')
        Config.set('other', 'jobs', '3')
        Config.set('other', 'verbose', '1')
        Config.set('other', 'ignored_categories', 
            "['outroduction', 'code']")
        Config.write(cfgfile)
        cfgfile.close()

GenerateConfig()
