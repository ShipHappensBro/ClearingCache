import Functions_Of_MainGui
import dearpygui.dearpygui as dpg
dpg.create_context()


with dpg.font_registry():
    with dpg.font(f'arialbi.ttf', 13, default_font=True, id="Default font"):
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
dpg.bind_font("Default font")


with dpg.window(label="Delete cache",modal=True,show=False,tag="cache_id",no_title_bar=True,width=360,height=100,pos=[120,200],no_move=True):           #Всплывающее окно кэша
    dpg.add_text("Все файлы кэша будут архивированы,а затем удалены\nВы уверены?")
    dpg.add_separator()
    with dpg.group(horizontal=True):
        cache_ok=dpg.add_button(label="OK",width=75,callback=Functions_Of_MainGui.button_cache,tag="cache_ok")
        dpg.add_button(label="Отмена",width=75,callback=lambda:dpg.configure_item("cache_id",show=False))


with dpg.window(label="Кэш 1С",no_move=True,no_close=True,no_resize=True,no_collapse=True):                                                             # ОКНО ОЧИСТКИ КЭША
    cache = dpg.add_button(label="Пересобрать",callback=lambda: dpg.configure_item("cache_id", show=True))


with dpg.window(label="Консоль",width=600,height=200,pos=[0,600],no_move=True,no_close=True,no_resize=True,no_collapse=True,tag='console'):             #Консоль
    dpg.add_separator()
    dpg.add_button(label='Очистить консоль',callback=Functions_Of_MainGui.console_cleared)
with dpg.window(label='Диспетчер печати',no_move=True,no_close=True,no_resize=True,no_collapse=True,pos=[100,0],width=130):
    dpg.add_button(label='Перезапуск',width=130,callback=lambda: dpg.configure_item('spooler_id',show=True))
    with dpg.window(label="Перезапуск диспетчера печати",modal=True,show=False,tag="spooler_id",no_title_bar=True,width=500,height=100,pos=[120,200],no_move=True):
        dpg.add_text('Диспетчер печати будет перезапущен,необходимы права администратора\nВы уверены?')
        dpg.add_separator()
        with dpg.group(horizontal=True):
            dpg.add_button(label='OK',callback=Functions_Of_MainGui.spooler_restart)
            dpg.add_button(label="Отмена",width=75,callback=lambda:dpg.configure_item("spooler_id",show=False))
dpg.create_viewport(title='Custom Title', width=600, height=800)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()