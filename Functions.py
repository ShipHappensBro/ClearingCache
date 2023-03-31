import os
import shutil
import time
class clearing_cache():
    def check_cache_roaming():
        roaming_path = os.path.expanduser('~\\AppData\\Roaming\\1C\\1cv8\\')
        if os.path.isdir(roaming_path):
            with os.scandir(roaming_path) as it:
                for entry in it:
                    if not entry.name.startswith('E') and entry.is_dir():
                        k=entry.name
                        current_username=os.getlogin()
                        date=time.strftime("%d.%m.%Y %H.%M ", time.localtime())
                        archive_name="ROAMING_"+str(date)+str(current_username)+"."+str(entry.name)
                        destroy_cache=str(roaming_path)+str(entry.name)
                        shutil.make_archive(base_name=archive_name,format='zip',base_dir=str(roaming_path)+str(entry.name),dry_run=False,)
                        shutil.rmtree(destroy_cache,ignore_errors=True)
                    elif entry.name.startswith('E') or entry.is_file:
                        print('ERROR:2 |Roaming| Cache wasnt found')   
            print('Directory was found_Roaming')
        elif roaming_path!=False:
            print('ERROR: 1_Roaming')
        else:
            print('Roaming success')
    def check_cache_local():
        local_path=os.path.expanduser('~\\AppData\\Local\\1C\\1cv8\\')
        if os.path.isdir(local_path):
            with os.scandir(local_path) as it:
                for entry in it:
                    if not entry.name.startswith('E') and entry.is_dir():
                        k=entry.name
                        current_username=os.getlogin()
                        date=time.strftime("%d.%m.%Y %H.%M ", time.localtime())
                        archive_name="LOCAL_"+str(date)+str(current_username) +"." +str(entry.name)
                        destroy_cache=str(local_path)+str(entry.name)
                        shutil.make_archive(base_name=archive_name,format='zip',base_dir=str(local_path)+str(entry.name))
                        shutil.rmtree(destroy_cache,ignore_errors=True)
                    else:
                        print("ERROR:2 |Local| Cache wasnt found")
            print("Directory was found_Local")            
        else:
            print("ERROR: 1_Local")