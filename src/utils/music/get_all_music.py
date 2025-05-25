def get_music():
  """
  Get all music files from the music directory.
  """
  import os

  music_dir = os.path.join(os.path.dirname(__file__), "..", "..", "music")
  print(music_dir)
  ls_dir = os.listdir(music_dir)
  return ls_dir
