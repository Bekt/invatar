# Invatar [![](https://circleci.com/gh/Bekt/invatar.svg?style=svg)](https://circleci.com/gh/Bekt/invatar)

Invatar provides an "API" for generating fully customizable SVG and image avatars 
with small text. Inspired from many messaging apps.

*Por que?* Por que no?

## Demo
Website: https://invatar0.appspot.com/

[Screenshots](http://i.imgur.com/9Ru5jZ1.png)


### Defaults

| [`svg/a.jpg`](https://invatar0.appspot.com/svg/a.jpg) | [`svg/kb.jpg`](https://invatar0.appspot.com/svg/kb.jpg) | [`svg/md.jpg`](https://invatar0.appspot.com/svg/md.jpg)
| --- | --- | --- |
| ![](https://invatar0.appspot.com/svg/a.jpg) | ![](https://invatar0.appspot.com/svg/kb.jpg) | ![](https://invatar0.appspot.com/svg/md.jpg)

### Customized

| `svg/a.jpg?s=150` | `svg/kb.jpg?s=150&color=yellow` | `svg/md.jpg?s=150&bg=%23E5E7E9&color=%23626262`
| --- | --- | --- |
| ![](https://invatar0.appspot.com/svg/a.jpg?s=150) | ![](https://invatar0.appspot.com/svg/kb.jpg?s=150&color=yellow) | ![](https://invatar0.appspot.com/svg/md.jpg?s=150&bg=%23E5E7E9&color=%23626262)
| Custom width/height (px) | Custom text color | Custom text color + background color. (`%23 == encodeURIComponent('#')`)


|  `svg/abcd.jpg?s=150&font_size=50` | `svg/kb.jpg?s=150&font_family=Monospace` | `svg/md.jpg?s=150&h=my-user-id`
| --- | --- | --- |
| ![](https://invatar0.appspot.com/svg/abcd.jpg?s=150&font_size=50) | ![](https://invatar0.appspot.com/svg/kb.jpg?s=150&font_family=Monospace) | ![](https://invatar0.appspot.com/svg/md.jpg?s=150&h=my-user-id`)
| Custom font size (in px)  | Custom font family | Provide a unique identifier with `h`. This is useful when you don't want two intials (different users?) hash to the same value.

## Use Cases

* Easier to identify users
* Friendlier than a "No avatar" picture
* Background colors are always consistent
* Can use as a fallback picture for Gravatar (`?default=` flag) and
  other similar services

## Contribution

Do it!

Currently the service is hosted on Google App Engine which is not my first choice. If you can
help with hosting, please reach out to me.

## Development

```bash
$ pip install -r dev-requirements.txt

# Running development server
$ python run.py

# Executing tests
$ tox
```

## License
MIT
