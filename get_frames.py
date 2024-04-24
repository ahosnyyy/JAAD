from jaad_data import JAAD
jaad_path = './'
imdb = JAAD(data_path=jaad_path)
imdb.extract_and_save_images()