from inference import InferencePipeline
from inference.core.interfaces.stream.sinks import render_boxes

api_key = "T9dyaU5pnxSWychmChZi"

pipeline = InferencePipeline.init(
    model_id="rock-paper-scissors-sxsw/11",
    video_reference=0,
    on_prediction = render_boxes,
    api_key=api_key,

)

pipeline.start()
pipeline.join()