# Neuro generative rt

![icon](icon.png)

#### W celu integracji z blenderem:
1. Projekt blendera należy umieścić w tam gdzie plik __blender_project_put_here.txt__
2. W otwartym projekcie blendera należy dodać plik __blends/geo_nodes.blend__ używając __File->Append...__
3. Podczas dodawania należy zaznaczyć opcję __Fake user__ wybierając elementy znajdujące się w katalogu __Materials__ (kolor_neuronu)
4. Podczas dodawania należy zaznaczyć opcję __Fake user__ wybierając elementy znajdujące się w katalogu __NodeTree__ (more_complex_saved_geo_node)
5. W otwartym projekcie w blenderze wskazać plik z __src/main.py__ i wystartować skrypt

#### Znane problemy:
- podczas uruchamiania skryptu, jeżeli [serwer (branch eeg)](https://github.com/rhoninn11/web_sd_monorepo/tree/eeg) wysyłający dane nie jest uruchomiony blender zatnie się aż do momentu jego uruchomienia
