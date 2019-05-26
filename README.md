# CuteGirls

Grab posts from some *booru sites. Written in Python 3.x.

## Supported sites
* [Danbooru](http://danbooru.donmai.us)
* [Gelbooru](https://gelbooru.com)
* [Konachan](http://konachan.com)
* [Rule34](https://rule34.xxx)
* [Yande.re](https://yande.re)

## Example
```python
from cutegirls import CuteGirls

cg = CuteGirls("gelbooru")

tags = ["kafuu_chino", "rating:safe"]
r = cg.search(tags=tags, limit=5, page=0)

post = r.posts[0]
print(post.file_url)

post.save_file()
```

## License
Made by molko.

See COPYING for more shit.
