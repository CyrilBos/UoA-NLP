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
        Config.add_section('other')
        Config.set('other', 'preprocess', 'False')
        Config.set('other', 'n_features', '20')
        Config.set('other', 'jobs', '3')
        Config.set('other', 'verbose', 'True')
        Config.set('other', 'ignored_categories', 
            "['outroduction', 'code']")
        Config.write(cfgfile)
        cfgfile.close()
