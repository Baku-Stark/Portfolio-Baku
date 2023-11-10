package Interface;

import java.awt.*;
import javax.swing.*;
import javax.swing.event.*;

public class PanelFooter extends JPanel{
	private static final long serialVersionUID = 1L;
	
	JPanel panel_west = new JPanel();
	JPanel panel_center = new JPanel();
	JPanel panel_east = new JPanel();
	
	GridBagConstraints c = new GridBagConstraints();
	GridBagConstraints c_info = new GridBagConstraints();

	PanelFooter(){
		this.setBackground(new Color(17, 17, 17));
		this.setPreferredSize(new Dimension(100, 105));
		this.setLayout(new GridLayout(1, 3));
		this.setOpaque(true);
		
		panel_west.setBackground(new Color(17, 17, 17));
		panel_center.setBackground(new Color(17, 17, 17));
		panel_east.setBackground(new Color(17, 17, 17));
		
		panel_west.setLayout(new GridBagLayout());
		
		c.fill = GridBagConstraints.HORIZONTAL;
		c.weightx = 0.8;
		c.gridx = 0;
		c.gridy = 0;
		panel_west.add(new FooterWest_IconMusic(), c);
		
		c_info.fill = GridBagConstraints.HORIZONTAL;
		c_info.weightx = 8;
		c_info.gridx = 1;
		c_info.gridy = 0;
		panel_west.add(new FooterWest_InfoMusic(), c_info);
		this.add(panel_west);
		// =====
		panel_center.setLayout(new GridLayout(2, 1));
		panel_center.add(new FooterCenter_Top());
		panel_center.add(new FooterCenter_Bot());
		this.add(panel_center);
		// =====
		panel_east.setLayout(new BorderLayout(10, 10));
		panel_east.add(new FooterEast(), BorderLayout.CENTER);
		this.add(panel_east);
	}
}

class FooterWest_IconMusic extends JPanel{
	private static final long serialVersionUID = 1L;
	
	JLabel icon = new JLabel();
	
	FooterWest_IconMusic(){
		this.setBackground(new Color(17, 17, 17));
		this.setLayout(new FlowLayout(FlowLayout.CENTER, FlowLayout.CENTER, 20));
		this.setOpaque(true);
		
		// =====
		icon.setBackground(new Color(17, 17, 17));
		icon.setIcon(new ImageIcon("src/Interface/buttons/disc.png"));
		icon.setOpaque(true);
		// =====
		
		this.add(icon);
	}
}

class FooterWest_InfoMusic extends JPanel{
	private static final long serialVersionUID = 1L;
	
	JLabel name_music = new JLabel("Music Name");
	JLabel album_music = new JLabel("Album");
	
	FooterWest_InfoMusic(){
		this.setLayout(new GridLayout(2, 1));
		this.setBackground(new Color(17, 17, 17));
		this.setOpaque(true);
		
		name_music.setFont(new Font("MV Boli", Font.PLAIN, 20));
		name_music.setBackground(new Color(17, 17, 17));
		name_music.setForeground(new Color(0xf0f8ff));
		// =====
		album_music.setFont(new Font("MV Boli", Font.PLAIN, 15));
		album_music.setBackground(new Color(17, 17, 17));
		album_music.setForeground(new Color(0xf0f8ff));
		
		this.add(name_music);
		this.add(album_music);
	}
}

class FooterCenter_Top extends JPanel{
	private static final long serialVersionUID = 1L;

	JSlider song_duration = new JSlider(0, 300);
	
	FooterCenter_Top(){
		this.setBackground(new Color(17, 17, 17));
		this.setOpaque(true);
		
		song_duration.setBackground(new Color(17, 17, 17));
		this.add(song_duration);
	}
}

class FooterCenter_Bot extends JPanel{
	private static final long serialVersionUID = 1L;
	
	JButton cicle =  new JButton();
	JButton shuffle = new JButton();
	
	JButton prev = new JButton();
	JButton play = new JButton();
	JButton next = new JButton();

	FooterCenter_Bot(){
		this.setLayout(new GridLayout(1, 3, 5, 5));
		this.setBackground(new Color(17, 17, 17));
		this.setOpaque(true);
		
		cicle.setBackground(new Color(17, 17, 17));
		cicle.setIcon(new ImageIcon("src/Interface/buttons/ciclo_none.png"));
		cicle.setOpaque(true);
		this.add(cicle);
		// =====
		prev.setBackground(new Color(17, 17, 17));
		prev.setIcon(new ImageIcon("src/Interface/buttons/prev.png"));
		prev.setOpaque(true);
		this.add(prev);
		// =====
		play.setBackground(new Color(17, 17, 17));
		play.setIcon(new ImageIcon("src/Interface/buttons/play.png"));
		play.setOpaque(true);
		add(this.play);
		// =====
		next.setBackground(new Color(17, 17, 17));
		next.setIcon(new ImageIcon("src/Interface/buttons/next.png"));
		next.setOpaque(true);
		this.add(next);
		// =====
		shuffle.setBackground(new Color(17, 17, 17));
		shuffle.setIcon(new ImageIcon("src/Interface/buttons/shuffle_none.png"));
		shuffle.setOpaque(true);
		this.add(shuffle);
	}
}

class FooterEast extends JPanel implements ChangeListener{
	private static final long serialVersionUID = 1L;
	
	int volume_max = 100;
	JLabel volume_text = new JLabel("Volume: " + volume_max);
	JSlider volume_slider = new JSlider(0, volume_max);
	
	FooterEast(){
		this.setLayout(new GridLayout(2, 1));
		this.setBackground(new Color(17, 17, 17));
		this.setOpaque(true);
		
		volume_slider.setValue(volume_max);
		volume_slider.addChangeListener(this);
		volume_slider.setBackground(new Color(17, 17, 17));
		this.add(volume_slider);
		
		volume_text.setForeground(new Color(0xf0f8ff));
		volume_text.setFont(new Font("MV Boli", Font.PLAIN, 25));
		volume_text.setHorizontalAlignment(JLabel.CENTER);
		this.add(volume_text);
		
		this.setVisible(true);
	}

	@Override
	public void stateChanged(ChangeEvent e) {
		// TODO Auto-generated method stub
		if(e.getSource() == volume_slider) {
			volume_text.setText("Volume: " + this.volume_slider.getValue());
		}
	}
}