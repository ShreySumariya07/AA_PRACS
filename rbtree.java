class Node {
    public int data;
    public int color;
    public Node parent;
    public Node right;
    public Node left;
}

public class rbtree {

    public Node NULL;
    public Node root;

    public rbtree() {
        NULL = new Node();
        NULL.color = 0;
        NULL.parent = null;
        NULL.right = NULL;
        NULL.left = NULL;
        root = NULL;
    }

    public void leftRotate(Node x) {
        Node y = x.right;
        x.right = y.left;
        if (y.left != null) {
            y.left.parent = x;
        }
        y.parent = x.parent;
        if (x.parent == null) {
            root = y;
        } else if (x == x.parent.right) {
            x.parent.right = y;
        } else {
            x.parent.left = y;
        }
        x.parent = y;
        y.left = x;
    }

    public void rightRotate(Node x) {
        Node y = x.left;
        x.left = y.right;
        if (y.right != null) {
            y.right.parent = x;
        }
        y.parent = x.parent;
        if (x.parent == null) {
            root = y;
        } else if (x == x.parent.right) {
            x.parent.right = y;
        } else {
            x.parent.left = y;
        }
        x.parent = y;
        y.right = x;
    }

    public void fix(Node k) {
        Node u;
        while (k.parent.color == 1) {
            if (k.parent == k.parent.parent.right) {
                u = k.parent.parent.left;
                if (u.color == 1) {
                    u.color = 0;
                    k.parent.color = 0;
                    k.parent.parent.color = 1;
                    k = k.parent;
                } else {
                    if (k == k.parent.left) {
                        k = k.parent;
                        rightRotate(k);
                    }
                    k.parent.color = 0;
                    k.parent.parent.color = 1;
                    leftRotate(k.parent.parent);
                }
            } else {
                u = k.parent.parent.right;
                if (u.color == 1) {
                    u.color = 0;
                    k.parent.color = 0;
                    k.parent.parent.color = 1;
                    k = k.parent;
                } else {
                    if (k == k.parent.right) {
                        k = k.parent;
                        leftRotate(k);
                    }
                    k.parent.color = 0;
                    k.parent.parent.color = 1;
                    rightRotate(k.parent.parent);
                }
            }
            if (root == k) {
                break;
            }
        }
        root.color = 0;
    }

    public void insert(int key) {
        Node node = new Node();
        node.data = key;
        node.color = 1;
        node.parent = null;
        node.left = NULL;
        node.right = NULL;

        Node x = this.root;
        Node y = null;

        while (x != NULL) {
            y = x;
            if (x.data > key) {
                x = x.left;
            } else {
                x = x.right;
            }
        }

        node.parent = y;

        if (node.parent == null) {
            root = node;
        } else if (y.data > node.data) {
            y.left = node;
        } else {
            y.right = node;
        }

        if (root == node) {
            node.color = 0;
            return;
        }

        if (node.parent.parent == null) {
            return;
        }

        fix(node);
    }

    public void print(Node node) {
        int i = 1;
        if (node != NULL) {
            System.out.println(node.data+"->"+node.color);
            print(node.left, "L", i);
            print(node.right, "R", i);
        }
        System.out.println();
    }

    public void print(Node node, String str, int i) {
        if (node != NULL) {
            System.out.println(node.data + " (" + str + "" + i + ") ");
            i++;
            print(node.left, "L", i);
            print(node.right, "R", i);
        }
    }

    public void printHelper() {
        print(this.root);
    }

    public static void main (String[] args) {
        rbtree rbt = new rbtree();
        rbt.insert(10);
        rbt.printHelper();
        rbt.insert(20);
        rbt.printHelper();
        rbt.insert(15);
        rbt.printHelper();
    }
}