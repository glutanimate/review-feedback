<!-- BANNER -->

Provides **feedback** for reviews by **flashing** a **small transparent image** at the center of your screen that varies between lapses and passed cards.

![](https://raw.githubusercontent.com/glutanimate/review-feedback/master/screenshots/zen.png)

### USAGE

The use of the Visual Feedback add-on is demonstrated in the following video (alongside other similar add-ons):

[![YouTube: Anki add-on guide: Gamify Your Reviews](https://i.ytimg.com/vi/UkveLkAgXiM/mqdefault.jpg)](https://youtu.be/UkveLkAgXiM)

Please note that some parts of the video (especially in regards to add-on configuration) are outdated since they were recorded on Anki 2.0.

### CONFIGURATION

You can configure the add-on by heading to Tools → Add-ons, selecting the add-on in the list, and then clicking on configure.

The settings you can adjust include:

- the *duration* time of the feedback image
- the *image set* to use

Additional image sets may be installed by placing a `lapsed.png` and `passed.png` file under `./user_files/images/_set-name_` where `_set_name_` is a name of your choice. Sets added in this way can then be chosen by setting them in the add-on configuration dialog.

E.g., if I wanted to add a new set called "basic", I would head to Tools → Add-ons, click on "Visual Feedback", click on "Open Add-ons folder", then create the `user_files` directory if it doesn't exist, create an `images` folder within that, and then place my `lapsed.png` and `passed.png` files in there. Then I would open the add-on's config window under Tools → Add-ons → Configure, and set `imageSet` to `basic`.

<!-- CHANGELOG -->

<!-- SUPPORT -->

### CREDITS AND LICENSE

*Copyright © 2017-2020 [Aristotelis P.](https://glutanimate.com/)  (Glutanimate)*

This is a fork of an add-on which was removed from AnkiWeb in early 2017. The original was most likely written by nest0r/Ja-Dark who [apparently deleted all of their shared Anki resources](https://web.archive.org/web/20190309073252/https://forum.koohii.com/thread-14570.html). There is no way to tell for sure since the original add-on description did not contain a copyright notice or attribution to a specific author.

Licensed under the _GNU AGPLv3_, extended by a number of additional terms. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY. For more information on the license please see the [LICENSE file](https://github.com/glutanimate/review-feedback/blob/master/LICENSE) accompanying this add-on and the [README](https://github.com/glutanimate/review-feedback/blob/master/README.md). The source code is available on [![GitHub icon](https://glutanimate.com/logos/github.svg) GitHub](https://github.com/glutanimate/review-feedback). Pull requests and other contributions are welcome!

<!-- RESOURCES -->

<!-- FUNDING -->
