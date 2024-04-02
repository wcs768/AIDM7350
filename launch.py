import gradio as gr
from suno import SongsGen

def greet(Lyric, Prompt):
    i = SongsGen('__client=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImNsaWVudF8yZUprUnl6QmhyWWFtUE9CdHFJTkdBTVVabVYiLCJyb3RhdGluZ190b2tlbiI6Im5rY3ZobWtxMGY5cjNnMDl5bGZiN2d6YzhzZDJxb3pxaXJwb3B3M3cifQ.hxPr_xf4_xbYpyq22n7ThcVyOhwCr-YxF8wfD_C5SuKnV5XN5s2Mja-TjsaHN2rD3bLE_dPe5juU7BUH6WfZ1hx9b7DIdjPHq_sapQTaQfEPQNISeW5x6P0V48CI-WxoczGSszSS8wyU8htaEJP-RiIt1YisrBejLJWS3xgEOrTrFJIv0c_HWwajRdKk8-Yl1xataCcdOp5TcQbq5ScwHcSaODaOyE99tfU6u9FTGT-VyiS1oy7YxHqk-1e07JxnJ6DMIlMDVXgtRYMcG5q4JjVPMAy4xveujNaGNL5-BzrgKFaZX6F0xifHZ-xIETDU3PbVsK4NQR91gAnI3Zywug; __client_uat=1711630067; mp_26ced217328f4737497bd6ba6641ca1c_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18e8519a765c81-076356e539630a-26001a51-100200-18e8519a765c81%22%2C%22%24device_id%22%3A%20%2218e8519a765c81-076356e539630a-26001a51-100200-18e8519a765c81%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; __cf_bm=h5h1.d1POpu0_MQFua2dw5ZJVcoHQill6sMSvp8mZK4-1711946774-1.0.1.1-YfmzNMd2gHh7Zz514d_bCgksIYCMlowFn9x6pes1OZ.BgRqjErN4iBzGtjB5yy9kQm4NYlMDe_Tx8q0ULffAlQ; _cfuvid=cPOqlM9ys74TCrIsiIfmKeddll9HrfmU0S_77aB7V4I-1711946774788-0.0.1.1-604800000') # Replace 'cookie'
    i.save_songs(Lyric, is_custom=True, title="custom", tags=Prompt)
    song = "output/suno_1.mp3"
    return song

demo = gr.Interface(
    fn=greet,
    inputs=["text", "text"],
    outputs=gr.Audio(type="numpy"),
)

demo.launch(share=True)
