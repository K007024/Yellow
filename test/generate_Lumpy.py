if __name__ == '__main__':
    from main import yellowGUI, yellow
    import os

    import swampy.Lumpy as Lp

    lumpy = Lp.Lumpy()
    lumpy.make_reference()

    obj = yellow.Yellow('../ressources')
    # obj = yellowGUI.YellowGUI()
    obj.lire()
    obj.afficher()

    lumpy.object_diagram()
    lumpy.class_diagram()
