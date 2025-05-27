
import gradio as gr
from interfaces import translate_multiline

CONFIG_MATRIX = [
    [
        ["kasumi", "香澄"],["tae", "多惠"],["rimi", "里美"],["saaya", "沙绫"],["arisa", "有咲"],
    ],
    [
        ["ran", "兰"],["moka", "摩卡"],["himari", "绯玛丽"],["tomo", "巴"],["tsugumi", "鸫"],
    ],
    [
        ["kokoro", "心"],["kaoru", "薰"],["hagumi", "育美"],["kanon", "花音"],["misaki", "美咲"],
    ],
    [
        ["aya", "彩"],["hina", "日菜"],["chisato", "千圣"],["maya", "麻弥"],["eve", "伊芙"],
    ],
    [
        ["yukina", "友希那"],["sayo", "纱夜"],["lisa", "莉莎"],["ako", "亚子"],["rinko", "燐子"],
    ],
    [
        ["mashiro", "真白"],["toko", "透子"],["nanami", "七深"],["tsukushi", "筑紫"],["rui", "瑠唯"],
    ],
    [
        ["layer", "瑞依"],["lock", "六花"],["masking", "益木"],["pareo", "PAREO"],["chuchu", "CHU²"],
    ],
    [
        ["tomori", "灯"],["anon", "爱音"],["rana", "乐奈"],["soyo", "素世"],["taki", "立希"],
    ],
]

def btn_fn(character_name_list = list):
    band = []
    for character_name in character_name_list:
        band.append(gr.Button(character_name, variant="secondary", scale=0, min_width=82))
    return band

def click_fn(character_btn, character_name = str):
    character_btn.click(lambda text: text + f"<{character_name}> ", inputs=input_text, outputs=input_text)

with gr.Blocks() as demo:
    gr.Markdown("## 邦邦对话风格化翻译器")

    with gr.Row():
        with gr.Column(scale=0, min_width=500):
            with gr.Row():
                poppin_party = btn_fn(character_name_list= [character_name[1] for character_name in CONFIG_MATRIX[0]])
                kasumi,tae,rimi,saaya,arisa = poppin_party
            with gr.Row():
                afterglow = btn_fn(character_name_list= [character_name[1] for character_name in CONFIG_MATRIX[1]])
                ran,moka,himari,tomo,tsugumi = afterglow
            with gr.Row():
                hello_happpy_world = btn_fn(character_name_list= [character_name[1] for character_name in CONFIG_MATRIX[2]])
                kokoro,kaoru,hagumi,kanon,misaki = hello_happpy_world
            with gr.Row():
                pastel_palettes = btn_fn(character_name_list= [character_name[1] for character_name in CONFIG_MATRIX[3]])
                aya,hina,chisato,maya,eve = pastel_palettes
        with gr.Column(scale=0, min_width=500):
            with gr.Row():
                roselia = btn_fn(character_name_list= [character_name[1] for character_name in CONFIG_MATRIX[4]])
                yukina,sayo,lisa,ako,rinko = roselia
            with gr.Row():
                morfonica = btn_fn(character_name_list= [character_name[1] for character_name in CONFIG_MATRIX[5]])
                mashiro,toko,nanami,tsukushi,rui = morfonica
            with gr.Row():
                raise_a_suilen = btn_fn(character_name_list= [character_name[1] for character_name in CONFIG_MATRIX[6]])
                layer,lock,masking,pareo,chuchu = raise_a_suilen
            with gr.Row():
                mygo = btn_fn(character_name_list= [character_name[1] for character_name in CONFIG_MATRIX[7]])
                tomori,anon,rana,soyo,taki = mygo
        with gr.Column():
            gr.Markdown("""
                        #### 输入样例: 
                            <kasumi> 哇，有咲今天的便当，看起来超级好吃的！\n
                            <arisa> 话说…… 你每天看我的便当，都要说看起来很好吃
                        """)

    with gr.Row():
        input_text = gr.Textbox(label="输入中文文本", placeholder="输入需要翻译的文本", lines=16)
        output_text = gr.Textbox(label="翻译结果", lines=16)
    
    with gr.Row():
        translate_button = gr.Button("翻译")

    with gr.Row():
        max_new_tokens_slider = gr.Slider(minimum=32, maximum=96, step=1, value=64, label="max_new_tokens")
        batch_size = gr.Slider(minimum=1, maximum=32, step=1, value=8, label="batch_size")

    with gr.Row():    
        temperature_slider = gr.Slider(minimum=0.3, maximum=1.5, step=0.05, value=0.75, label="temperature")
        top_p_slider = gr.Slider(minimum=0.5, maximum=1.0, step=0.05, value=0.9, label="top_p")
        repetition_penalty = gr.Slider(minimum=1.0, maximum=2.0, step=0.05, value=1.2, label="repetition_penalty")
    
    for band_numo,band in enumerate([poppin_party, afterglow, hello_happpy_world, pastel_palettes, roselia, morfonica, raise_a_suilen, mygo]):
        for numo,character in enumerate(band):
            click_fn(character_btn=character, character_name=CONFIG_MATRIX[band_numo][numo][0])
    
    translate_button.click(fn=translate_multiline, inputs=[input_text, max_new_tokens_slider, batch_size, repetition_penalty, temperature_slider, top_p_slider], outputs=output_text)

demo.launch(share=True)