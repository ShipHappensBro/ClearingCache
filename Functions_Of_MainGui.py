import dearpygui.dearpygui as dpg
import Functions
import Functions_Of_WinPy
def console_cleared():
    dpg.delete_item(item='console')
    with dpg.window(label="Консоль",width=600,height=200,pos=[0,600],no_move=True,no_close=True,no_resize=True,no_collapse=True,tag='console'):
        dpg.add_separator()
        dpg.add_button(label='Очистить консоль',callback=console_cleared)
def button_cache():
    clearing_cache=Functions.clearing_cache.check_cache_roaming() ,Functions.clearing_cache.check_cache_local(),dpg.configure_item("cache_id", show=False),dpg.add_text('Кэш очищен',parent='console')
def spooler_restart():
    restart=Functions_Of_WinPy.restart_services.restart_spooler(),dpg.configure_item('spooler_id',show=False),dpg.add_text('Диспетчер перезапущен',parent='console')