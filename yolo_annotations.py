from jaad_data import JAAD
jaad_path = './'
imdb = JAAD(data_path=jaad_path)
imdb.get_detection_data(image_set='train', method='yolo4', occlusion_type='un-full', file_path='data-un-full/')