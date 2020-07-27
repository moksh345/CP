
class Node {
    public int value;
    public Node left, right;
    public Node(int value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

public class BST {
    public Node root;
    
    public BST(int value) {
        this.root = new Node(value);
    }

    public void insert(int value) {
        // Your code goes here
        Node node=this.root;
        this.root=insert(node,value);
    }

    private Node insert(Node node, int value) {
        // Your code goes here
        if (node==null) return new Node(value);
        if( value< node.value){
            node.left=insert(node.left,value);
        }
        else if (value>node.value){
            node.right=insert(node.right,value);
        }
        else{
            node.value=value;
        }
        return node;
    }

    public boolean search(int value) {
        // Your code goes here
        boolean x= search(this.root,value);

    	return x;
    }

    private boolean search(Node current, int value) {
        // Your code goes here
        boolean x;
        if(value>current.value){
            if(current.right==null){
                return false;
            }
            x=search(current.right,value);
        }else if(value<current.value){
            if(current.left==null){
                return false;
            }
            x=search(current.left,value);
        }else{return true;}
    	return x;
    }

}